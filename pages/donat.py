from config.conftest import *

@pytest.fixture()
def donats(page: Page):
    def page_donations():
        page.goto("https://metanit.com/")
        page.click('//*[@id="header"]/div[2]/ul/li[2]/a')
        page.wait_for_url("https://metanit.com/donations.php")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
        expect(page).to_have_url("https://metanit.com/")
    return page_donations