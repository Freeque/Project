import Config as config
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import unittest
import time


class AllTests(unittest.TestCase):


    def test_gallery_view_Positive(self):
        driver = webdriver.Chrome()
        config.website_login(driver)

        config.wait_and_click(driver, By.XPATH, "//span[@title='DataFolderA']")
        config.wait_and_click(driver, By.XPATH, "//span[@title='DataFolderB']")
        config.wait_and_click(driver, By.XPATH, "//span[@title='DataFolderC1']")
        config.wait_and_click(driver, By.XPATH, "//button[@data-mode='gallery']']")
        time.sleep(2)
        config.wait_and_click(driver, By.XPATH, "//div[@class='gallery-item ui-selectee']")
        num = len(driver.find_elements_by_xpath("//div[@class='gallery-item ui-selectee']"))
        assert num == 4
        print("working fine")
        driver.close()


    def test_logging_in_Negative(self):
        driver = webdriver.Chrome()
        config.website_login(driver)

        config.wait_and_click(driver, By.XPATH, "//button[@data-bind-hide='m.isUserLoggedIn']")
        config.wait_and_click(driver, By.ID, "loginUsername")
        el = driver.find_element(By.ID, "loginUsername")
        el.send_keys(config.login["username"])
        el.send_keys(Keys.RETURN)
        state = el.is_displayed()
        assert state is True
        print("working fine")
        driver.close()

    def test_gallery_view_Negative(self):
        driver = webdriver.Chrome()
        config.website_login(driver)

        wait = WebDriverWait(driver, 10)
        config.wait_and_click(driver, By.XPATH, "//span[@title='DataFolderA']")
        config.wait_and_click(driver, By.XPATH, "//span[@title='DataFolderB']")
        config.find_and_wait(driver, By.XPATH, "//span[@title='DataFolderC1']")
        config.wait_and_click(driver, By.XPATH, "//button[@data-mode='gallery']")
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//a[@class='dropdown-toggle']")))
        el = driver.find_element_by_xpath("//div[@class='gallery-empty']")
        state = el.is_displayed()
        print(state)
        assert state is True
        print("working fine")
        driver.close()

    def test_downloading_1_file(self):
        driver = webdriver.Chrome()
        config.website_login(driver)

        config.wait_and_click(driver, By.XPATH, "//span[@title='DataFolderA']")
        config.wait_and_click(driver, By.XPATH, "//span[@title='DataFolderB']")
        config.wait_and_click(driver, By.XPATH, "//span[@title='DataFolderC2']")
        config.wait_and_click(driver, By.XPATH, "//div[@class='type folder-item file spreadsheet-microsoft has-preview']//div[@class='inner-wrapper']")
        config.wait_and_click(driver, By.XPATH, "//button[@class='btn btn-primary btn-block folderLink-buttons-download is-type-selected']")
        driver.get("chrome://downloads/")
        manager = driver.find_element_by_css_selector('body/deep/downloads-manager')
        item = manager.find_element_by_css_selector('body/deep/downloads-item')
        shadow = driver.execute_script('return arguments[0].shadowRoot;', item)
        link = shadow.find_element_by_css_selector('div#title-area>a')
        if config.login["filename"] in link.text:
            print(link.text)
            assert True
            os.remove(config.login["downloads"]+config.login["filename"])
            print("working fine")
        else:
            assert False
        driver.close()

    def test_downloading_multiple_files(self):
        driver = webdriver.Chrome()
        config.website_login(driver)

        config.wait_and_click(driver, By.XPATH, "//span[@title='DataFolderA']")
        config.wait_and_click(driver, By.XPATH, "//span[@title='DataFolderB']")
        config.wait_and_click(driver, By.XPATH, "//span[@title='DataFolderC2']")
        config.wait_and_click(driver, By.XPATH, "//div[@class='type folder-item file spreadsheet-microsoft has-preview']//div[@class='inner-wrapper']")
        config.wait_and_click(driver, By.XPATH, "//div[@class='type folder-item file pdf has-preview']//div[@class='inner-wrapper']")
        config.wait_and_click(driver, By.XPATH, "//button[@class='btn btn-primary btn-block folderLink-buttons-download is-type-selected']")
        time.sleep(1)
        driver.get("chrome://downloads/")
        manager = driver.find_element_by_css_selector('body/deep/downloads-manager')
        item = manager.find_element_by_css_selector('body/deep/downloads-item')
        shadow = driver.execute_script('return arguments[0].shadowRoot;', item)
        link = shadow.find_element_by_css_selector('div#title-area>a')
        if config.login["foldername"] in link.text:
            print(link.text)
            assert True
            os.remove(config.login["downloads"] + config.login["foldername"])
            print("working fine")
        else:
            assert False
        driver.close()



suite = unittest.TestLoader().loadTestsFromTestCase(AllTests)
unittest.TextTestRunner(verbosity=1).run(suite)