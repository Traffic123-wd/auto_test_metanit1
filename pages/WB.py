from config.conftest import *

@pytest.fixture()
def btn_wb(page: Page):
    def page_wb():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[5]/a')
        page.wait_for_url("https://metanit.com/web/")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        page.wait_for_timeout(1000)
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_wb