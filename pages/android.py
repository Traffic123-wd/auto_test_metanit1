from config.conftest import *

@pytest.fixture()
def androids(page:Page):
    def page_android():
        page.goto("https://metanit.com/")
        page.click('//*[@id="header"]/div[2]/ul/li[5]/a')
        page.wait_for_url("https://metanit.com/android.php")
        page.wait_for_timeout(1000)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[1]/p/a')
        page.wait_for_url("https://www.rustore.ru/catalog/app/com.metanit.python_tutorial_full")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/android.php")
        page.wait_for_timeout(1000)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[2]/p/a')
        page.wait_for_url("https://www.rustore.ru/catalog/app/com.metanit.python_tutorial")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/android.php")
        page.wait_for_timeout(1000)
        page.click('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[3]/p/a')
        page.wait_for_url("https://play.google.com/store/apps/details?id=com.metanit.python_tutorial")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/android.php")
        page.wait_for_timeout(1000)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        page.wait_for_timeout(1000)
    return page_android

