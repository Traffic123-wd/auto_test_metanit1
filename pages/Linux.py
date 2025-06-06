from config.conftest import *

@pytest.fixture()
def btn_linux1(page: Page):
    def page_Linux1():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[18]/a')
        page.wait_for_url("https://metanit.com/os/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_Linux1

@pytest.fixture()
def btn_linux2(page: Page):
    def page_Linux2():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[18]/a')
        page.wait_for_url("https://metanit.com/os/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/p[1]/a')
        page.wait_for_url("https://metanit.com/os/linux/12.1.php")
        time.sleep(1)
        page.goto("https://metanit.com/os/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_Linux2

@pytest.fixture()
def btn_linux3(page: Page):
    def page_Linux3():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[18]/a')
        page.wait_for_url("https://metanit.com/os/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/p[1]/a')
        page.wait_for_url("https://metanit.com/os/linux/12.1.php")
        time.sleep(1)
        page.click('//*[@id="browser"]/li[1]/span')
        time.sleep(1)
        page.click('//*[@id="browser"]/li[1]/ul/li[1]/span/a')
        page.wait_for_url("https://metanit.com/os/linux/1.1.php")
        time.sleep(1)
        page.goto("https://metanit.com/os/linux/12.1.php")
        time.sleep(1)
        page.goto("https://metanit.com/os/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_Linux3

@pytest.fixture()
def btn_linux4(page: Page):
    def page_Linux4():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[18]/a')
        page.wait_for_url("https://metanit.com/os/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/p[1]/a')
        page.wait_for_url("https://metanit.com/os/linux/12.1.php")
        time.sleep(1)
        page.click('//*[@id="browser"]/li[1]/span')
        time.sleep(1)
        page.click('//*[@id="browser"]/li[1]/ul/li[2]/span/a')
        page.wait_for_url("https://metanit.com/os/linux/1.2.php")
        time.sleep(1)
        page.goto("https://metanit.com/os/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_Linux4

