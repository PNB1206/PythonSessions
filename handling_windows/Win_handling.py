from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def handling_windows():
    driver =webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://chercher.tech/python/windows-selenium-python")
    driver.implicitly_wait(25)

    print('Parent window title is: ', driver.title)

    parent_handle = driver.current_window_handle
    wait = WebDriverWait(driver, 30)
    wait.until(expected_conditions.element_to_be_clickable(By.XPATH, "//a[@title='alerts-selenium-python']")).click()


    #driver.find_element_by_xpath("//a[@title='alerts-selenium-python']").click()

    child_handles = driver.window_handles
    print(len(child_handles))

    for child in child_handles:
        if child != parent_handle:
            driver.switch_to.window(child)
            print('Chile window title is: ', driver.title)
            driver.close()

wh = handling_windows()