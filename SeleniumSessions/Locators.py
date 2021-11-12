import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager


class Test_Locators:

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://smartmoney.clarksfield.com/login/")

    def test_locatores(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.delete_all_cookies()
        driver.get("")
        driver.fullscreen_window()

        passwordField = driver.find_element(By.ID, "input_password")
        passwordField.send_keys("qazplmq1w2e3r4")

        emailField = driver.find_element(locate_with(By.TAG_NAME, 'input').above(passwordField))
        emailField.send_keys("nagendra@scaledesk.xyz")

        driver.find_element(locate_with(By.TAG_NAME, "button").below(passwordField)).click()
        driver.minimize_window()
        time.sleep(3)
        driver.quit()

    setUp()
    test_locatores()
