import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(20)
driver.get("https://smartmoney.angelone.in/login/")
driver.delete_all_cookies()
#driver.switch_to.alert.dismiss()
emai_id ='input__email'
password_id = "input_password"
loginBtn_xpath = "//span[normalize-space()='Login Now']"

driver.find_element(By.ID,emai_id).send_keys('nagendra@scaledesk.xyz')
driver.find_element(By.ID,password_id).send_keys('Test@12345')
driver.find_element(By.XPATH,loginBtn_xpath).click()
print(driver.title)
driver.save_screenshot('./SMLogin_403Error.png')
time.sleep(3)