from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class logingPage:

    searchbox = (By.XPATH, "//input[@type='text']")
    text = "Pytest framework"

    def __init__(self, driver):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://www.google.com/')


    def enterText_searchbox(self):
        self.driver.find_element(self.searchbox).send_keys(self.text)

