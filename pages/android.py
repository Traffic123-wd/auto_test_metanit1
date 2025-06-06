from config.conftest import *

@pytest.fixture()
def androids1(page:Page):
    def page_android1():
        page.goto("https://metanit.com/")
        page.click('//*[@id="header"]/div[2]/ul/li[5]/a')
        page.wait_for_url("https://metanit.com/android.php")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_android1

@pytest.fixture()
def androids2(page: Page):
    def page_android2():
        page.goto("https://metanit.com/")
        page.click('//*[@id="header"]/div[2]/ul/li[5]/a')
        page.wait_for_url("https://metanit.com/android.php")
        page.wait_for_timeout(1000)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/p/a')
        page.wait_for_url("https://www.rustore.ru/catalog/app/com.metanit.python_tutorial_full")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/android.php")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_android2

@pytest.fixture()
def androids3(page: Page):
    def page_android3():
        page.goto("https://metanit.com/")
        page.click('//*[@id="header"]/div[2]/ul/li[5]/a')
        page.wait_for_url("https://metanit.com/android.php")
        page.wait_for_timeout(1000)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/p/a')
        page.wait_for_url("https://www.rustore.ru/catalog/app/com.metanit.python_tutorial")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/android.php")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_android3

@pytest.fixture()
def androids4(page: Page):
    def page_android4():
        page.goto("https://metanit.com/")
        page.click('//*[@id="header"]/div[2]/ul/li[5]/a')
        page.wait_for_url("https://metanit.com/android.php")
        page.wait_for_timeout(1000)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]/p/a')
        page.wait_for_url("https://play.google.com/store/apps/details?id=com.metanit.python_tutorial")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/android.php")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_android4

