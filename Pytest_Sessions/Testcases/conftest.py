import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(scope='class')
def init_driver(request):
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    web_driver.maximize_window()
    web_driver.get("https://www.programiz.com/python-programming/online-compiler/")
    web_driver.set_page_load_timeout(30)
    web_driver.delete_all_cookies()

    request.cls.driver = web_driver

    yield
    web_driver.close()