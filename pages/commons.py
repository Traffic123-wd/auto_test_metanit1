from config.conftest import *

@pytest.fixture()
def com_page1(page: Page):
    def page_common1():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[1]/a')
        page.wait_for_url("https://metanit.com/common/")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_common1

@pytest.fixture()
def com_page2(page: Page):
    def page_common2():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[1]/a')
        page.wait_for_url("https://metanit.com/common/")
        page.wait_for_timeout(1000)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/p[1]/a')
        page.wait_for_timeout(1000)
        page.goto('https://metanit.com/common/')
        page.wait_for_timeout(1000)
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_common2

@pytest.fixture()
def com_page3(page: Page):
    def page_common3():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[1]/a')
        page.wait_for_url("https://metanit.com/common/")
        page.wait_for_timeout(1000)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[2]/div/div/p[3]/a')
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/common/")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_common3

@pytest.fixture()
def com_page4(page: Page):
    def page_common4():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[2]/a')
        page.wait_for_url("https://metanit.com/assembler/")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_common4

@pytest.fixture()
def com_page5(page: Page):
    def page_common5():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[2]/a')
        page.wait_for_url("https://metanit.com/assembler/")
        page.wait_for_timeout(1000)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[1]/p[5]/a')
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/assembler/")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_common5

@pytest.fixture()
def com_page6(page: Page):
    def page_common6():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[2]/a')
        page.wait_for_url("https://metanit.com/assembler/")
        page.wait_for_timeout(1000)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[1]/p[6]/a')
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/assembler/")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_common6

@pytest.fixture()
def com_page7(page: Page):
    def page_common7():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[2]/a')
        page.wait_for_url("https://metanit.com/assembler/")
        page.wait_for_timeout(1000)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[1]/p[7]/a')
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/assembler/")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_common7

@pytest.fixture()
def com_page8(page: Page):
    def page_common8():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[2]/a')
        page.wait_for_url("https://metanit.com/assembler/")
        page.wait_for_timeout(1000)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/div[1]/p[8]/a')
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/assembler/")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_common8
