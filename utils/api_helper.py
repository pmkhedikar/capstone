from playwright.sync_api import APIRequestContext, sync_playwright, APIResponse
from features.variables import API_URL

class APIClient:
    def __init__(self, base_url=API_URL):
        self._playwright = sync_playwright().start()
        self.request_context: APIRequestContext = self._playwright.request.new_context(base_url=base_url)

    def get(self, endpoint: str, **kwargs) -> APIResponse:
        return self.request_context.get(endpoint, **kwargs)

    def post(self, endpoint: str, data=None, **kwargs) -> APIResponse:
        return self.request_context.post(endpoint, data=data, **kwargs)

    def close(self):
        self.request_context.dispose()
        self._playwright.stop()