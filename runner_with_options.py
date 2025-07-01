from behave.__main__ import main

if __name__ == "__main__":
    browser = "chromium"      # 'chromium', 'firefox', 'webkit'
    headless = "false"        # true/false
    tags = "@login"      # e.g. "@login"
    feature_file_path = "features/"

    main([
        '--define', f'browser={browser}',
        '--define', f'headless={headless}',
        '--tags', tags,
        feature_file_path,
        # '--format=allure_behave.formatter:AllureFormatter',
        # '--outputfile=allure-results',
    ])