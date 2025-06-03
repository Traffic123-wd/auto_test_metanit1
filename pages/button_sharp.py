from config.conftest import *

@pytest.fixture()
def btn_sharp(page: Page):
    def page_sharp():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[3]/a')
        page.wait_for_url("https://metanit.com/sharp/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[1]/p[2]/a')
        time.sleep(1)
        page.goto("https://metanit.com/sharp/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[1]/p[3]/a')
        time.sleep(1)
        page.goto("https://metanit.com/sharp/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[1]/p[4]/a')
        time.sleep(1)
        page.goto("https://metanit.com/sharp/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[1]/p[5]/a')
        time.sleep(1)
        page.goto("https://metanit.com/sharp/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
    return page_sharp