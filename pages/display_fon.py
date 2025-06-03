from config.conftest import *

@pytest.fixture()
def display(page: Page):
    def page_display_fon(page: Page):
        page.goto("https://metanit.com/")
        page.click('//*[@id="toggle-theme"]')
        page.wait_for_timeout(1000)
        page.click('//*[@id="toggle-theme"]')
        page.wait_for_timeout(1000)
    return page_display_fon