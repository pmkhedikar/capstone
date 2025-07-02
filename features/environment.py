import os
import shutil
from playwright.sync_api import sync_playwright
from allure_commons._allure import attach
from allure_commons.types import AttachmentType
from datetime import datetime
from utils.logger import GenericLogger
from utils.api_helper import APIClient

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
logger = GenericLogger().logger

def before_all(context):
    # Clean up old artifacts
    for repo in ['logs', 'screenshots', 'videos']:
        if os.path.exists(repo):
            shutil.rmtree(repo)
    os.makedirs('screenshots', exist_ok=True)
    os.makedirs('videos', exist_ok=True)
    os.makedirs('logs', exist_ok=True)

    test_type = context.config.userdata.get('test_type', 'ui').lower()
    context.test_type = test_type

    if test_type == "ui":
        context.playwright = sync_playwright().start()
        browser_name = context.config.userdata.get('browser', 'chromium')
        headless = context.config.userdata.get('headless', 'true').lower() == 'true'
        context.browser = getattr(context.playwright, browser_name).launch(headless=headless)
    elif test_type == "api":
        context.api_client = APIClient()

def before_scenario(context, scenario):
    if getattr(context, "test_type", "ui") == "ui":
        context.context = context.browser.new_context(record_video_dir="videos/")
        context.page = context.context.new_page()

def after_scenario(context, scenario):
    if getattr(context, "test_type", "ui") == "ui":
        if scenario.status == "failed":
            logger.error(f"Scenario failed: {scenario.name}")
            screenshot_path = f"screenshots/{scenario.name.replace(' ', '_')}_{timestamp}.png"
            context.page.screenshot(path=screenshot_path)
            with open(screenshot_path, "rb") as image_file:
                attach(image_file.read(), name=f"Screenshot: {scenario.name}", attachment_type=AttachmentType.PNG)

            video_path = context.page.video.path()
            context.page.close()
            context.context.close()
            if os.path.exists(video_path):
                with open(video_path, "rb") as video_file:
                    attach(video_file.read(), name=f"Video: {scenario.name}", attachment_type=AttachmentType.WEBM)
        else:
            context.page.close()
            context.context.close()

def after_all(context):
    logger.info("Test run completed. Cleaning up browser and Playwright.")
    if getattr(context, "test_type", "ui") == "ui":
        if hasattr(context, 'browser'):
            context.browser.close()
        if hasattr(context, 'playwright'):
            context.playwright.stop()
    elif getattr(context, "test_type", "ui") == "api":
        if hasattr(context, 'api_client'):
            context.api_client.close()