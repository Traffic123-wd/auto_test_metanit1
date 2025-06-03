from config.conftest import *

@pytest.fixture()
def vk_page(page: Page):
    def page_VK():
        page.goto("https://metanit.com/")
        page.click('//*[@id="header"]/div[2]/ul/li[3]/a')
        page.wait_for_url("https://vk.com/metanit")
        page.wait_for_timeout(3000)
        page.fill('//*[@id="search-:r0:"]', 'Romanov')
        page.press('//*[@id="search-:r0:"]', 'Enter')
        page.wait_for_timeout(3000)
        page.goto("https://vk.com/metanit")
        page.wait_for_timeout(3000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(3000)
    return page_VK