from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


## Sensitive data
login = {
    "url": "https://qarecruitment.egnyte.com/fl/MI3vaEWqBQ",
    "password": "[PASSWORD]",
    "username": "[USERNAME]",
    "downloads": "[PATH TO DOWNLOADS FOLDER]",
    "filename": "[FILE NAME]",
    "foldername": "[FOLDER NAME]",

}


def wait_and_click(driver, method, value):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((method, value))).click()


def find_and_wait(driver, method, value):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((method, value)))


def website_login(driver):
    driver.get(login["url"])
    password = driver.find_element(by="id", value='password')
    password.clear()
    password.send_keys(login["password"])
    password.send_keys(Keys.RETURN)







