from config.conftest import *

@pytest.fixture()
def enter_page(page: Page):
    def enter_page_mtn():
        page.goto("https://metanit.com/")
        page.wait_for_timeout(2000)
        expect(page).to_have_url("https://metanit.com/")
    return enter_page_mtn