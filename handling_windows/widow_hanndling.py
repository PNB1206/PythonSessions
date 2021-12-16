import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Handling_wondows_Test:
    def setup(self):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://smartmoney.clarksfield.com/login/')
        driver.pa
    def test_handlig_idows(self):
        driver.get





    def tearDown(self):
        time.sleep(5)
        driver.quit()