from config.conftest import *

@pytest.fixture()
def finds(page: Page):
    def page_find():
        page.goto("https://metanit.com/")
        page.click('//*[@id="magnifying-glass"]')
        page.wait_for_timeout(1000)
        page.click('//*[@id="magnifying-glass"]')
        page.goto("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_find