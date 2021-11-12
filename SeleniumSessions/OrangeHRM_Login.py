import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager


class OrangeHRM_Login_Test:

       def test_orangeHRM_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")

        driver.implicitly_wait(25)
        """ Enter Password"""
        password_field = driver.find_element(By.ID, 'txtPassword')
        password_field.send_keys("admin123")

        """ Enter username"""
        driver.find_element(locate_with(By.TAG_NAME,'input').above(password_field)).send_keys('Admin')
        time.sleep(3)

        """ Click on Login button"""
        driver.find_element(locate_with(By.TAG_NAME, 'input').below(password_field)).click()

        """Get the title after login"""
        title = driver.title
        assert title == "OrangeHRM", "Test case failed"


hrm = OrangeHRM_Login_Test()
hrm.test_orangeHRM_login()



