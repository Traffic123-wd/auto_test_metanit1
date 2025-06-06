from config.conftest import *

@pytest.fixture()
def btn_sharp1(page: Page):
    def page_sharp1():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[3]/a')
        page.wait_for_url("https://metanit.com/sharp/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_sharp1

@pytest.fixture()
def btn_sharp2(page: Page):
    def page_sharp2():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[3]/a')
        page.wait_for_url("https://metanit.com/sharp/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[1]/p[2]/a')
        time.sleep(1)
        page.goto("https://metanit.com/sharp/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_sharp2

@pytest.fixture()
def btn_sharp3(page: Page):
    def page_sharp3():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[3]/a')
        page.wait_for_url("https://metanit.com/sharp/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[1]/p[3]/a')
        time.sleep(1)
        page.goto("https://metanit.com/sharp/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_sharp3

@pytest.fixture()
def btn_sharp4(page: Page):
    def page_sharp4():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[3]/a')
        page.wait_for_url("https://metanit.com/sharp/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[1]/p[4]/a')
        time.sleep(1)
        page.goto("https://metanit.com/sharp/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_sharp4

@pytest.fixture()
def btn_sharp5(page: Page):
    def page_sharp5():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[3]/a')
        page.wait_for_url("https://metanit.com/sharp/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[1]/p[5]/a')
        time.sleep(1)
        page.goto("https://metanit.com/sharp/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
    return page_sharp5