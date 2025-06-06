from config.conftest import *

@pytest.fixture()
def btn_cpp1(page: Page):
    def page_c_2plus1():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[8]/a')
        page.wait_for_url("https://metanit.com/cpp/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_c_2plus1

@pytest.fixture()
def btn_cpp2(page: Page):
    def page_c_2plus2():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[8]/a')
        page.wait_for_url("https://metanit.com/cpp/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[2]/div/a[1]')
        page.wait_for_url("https://metanit.com/cpp/tutorial/")
        time.sleep(1)
        page.goto("https://metanit.com/cpp/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_c_2plus2

@pytest.fixture()
def btn_cpp3(page: Page):
    def page_c_2plus3():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[8]/a')
        page.wait_for_url("https://metanit.com/cpp/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[2]/div/a[2]')
        page.wait_for_url("https://metanit.com/cpp/qt/")
        time.sleep(1)
        page.goto("https://metanit.com/cpp/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_c_2plus3

@pytest.fixture()
def btn_cpp4(page: Page):
    def page_c_2plus4():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[8]/a')
        page.wait_for_url("https://metanit.com/cpp/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[2]/div/a[3]')
        page.wait_for_url("https://metanit.com/cpp/vulkan/")
        time.sleep(1)
        page.goto("https://metanit.com/cpp/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        time.sleep(1)
        expect(page).to_have_url("https://metanit.com/")
    return page_c_2plus4
