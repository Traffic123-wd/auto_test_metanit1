from config.conftest import *

@pytest.fixture()
def btn_sql1(page: Page):
    def page_SQL1():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[9]/a')
        page.wait_for_url("https://metanit.com/sql/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_SQL1

@pytest.fixture()
def btn_sql2(page: Page):
    def page_SQL2():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[9]/a')
        page.wait_for_url("https://metanit.com/sql/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[2]/div/a[1]')
        page.wait_for_url("https://metanit.com/sql/sqlserver/")
        time.sleep(1)
        page.goto("https://metanit.com/sql/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_SQL2

@pytest.fixture()
def btn_sql3(page: Page):
    def page_SQL3():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[9]/a')
        page.wait_for_url("https://metanit.com/sql/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[2]/div/a[2]')
        page.wait_for_url("https://metanit.com/sql/postgresql/")
        time.sleep(1)
        page.goto("https://metanit.com/sql/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_SQL3

@pytest.fixture()
def btn_sql4(page: Page):
    def page_SQL4():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[9]/a')
        page.wait_for_url("https://metanit.com/sql/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[2]/div/a[3]')
        page.wait_for_url("https://metanit.com/sql/mysql/")
        time.sleep(1)
        page.goto("https://metanit.com/sql/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        expect(page).to_have_url("https://metanit.com/")
        time.sleep(1)
    return page_SQL4

@pytest.fixture()
def btn_sql5(page: Page):
    def page_SQL5():
        page.goto("https://metanit.com/")
        page.click('//*[@id="menu"]/ul/li[9]/a')
        page.wait_for_url("https://metanit.com/sql/")
        time.sleep(1)
        page.click('//*[@id="container"]/div[1]/div[1]/div[2]/div/a[4]')
        page.wait_for_url("https://metanit.com/sql/sqlite/")
        time.sleep(1)
        page.goto("https://metanit.com/sql/")
        time.sleep(1)
        page.goto("https://metanit.com/")
        time.sleep(1)
        expect(page).to_have_url("https://metanit.com/")
    return page_SQL5