from playwright.sync_api import Page
from pages.components.globals.alert_component import AlertComponent

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.alert = AlertComponent(page)

    def navigate(self, url):
        self.page.goto(url)

    def click_until_visible(self, locator_to_click, locator_to_wait, max_retries=3, timeout=2000):
        for _ in range(max_retries):
            try:
                locator_to_click.click()
                locator_to_wait.wait_for(state="visible", timeout=timeout)
                return
            except:
                continue
        # If it fails after all retries, try one last time and let it fail normally if it must
        locator_to_click.click()
        locator_to_wait.wait_for(state="visible", timeout=timeout)

    