# Last tested 3/11/2021 14:16

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from decouple import config
import unittest, time, re

Username = config("DOCS_USERNAME", cast=str)
Password = config("DOCS_PASSWORD", cast=str)
ProductSlug = config("PRODUCT_SLUG", cast=str)

class UntitledTestCase8(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(config("DRIVER_PATH", cast=str))
        # self.driver = webdriver.Chrome(config("DRIVER_PATH", cast=str))
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case8(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://staging-product.superyou.co.id/docs") # Website Link
        time.sleep(1)
        
        # Login
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/section/div/button").click() # Click Authroize Button
        driver.find_element_by_id("oauth_username").click() # Click username field
        driver.find_element_by_id("oauth_username").clear()
        driver.find_element_by_id("oauth_username").send_keys(Username) # Enter username
        driver.find_element_by_id("oauth_password").clear()
        driver.find_element_by_id("oauth_password").send_keys(Password) # Enter password
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/section/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[4]/button[1]").click() # Click authorize button
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/section/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[3]/button[2]").click() # Click close button
        time.sleep(2)

        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[4]/section/div/span[2]/div/div/div/span[6]/div/div[1]").click() # Click GET read product by slug
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[4]/section/div/span[2]/div/div/div/span[6]/div/div[2]/div/div[1]/div[1]/div[2]/button").click() # Click Try it Out button
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[4]/section/div/span[2]/div/div/div/span[6]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/input").click() # Press product slug field
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[4]/section/div/span[2]/div/div/div/span[6]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/input").clear()
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[4]/section/div/span[2]/div/div/div/span[6]/div/div[2]/div/div[1]/div[2]/div/table/tbody/tr[1]/td[2]/input").send_keys(ProductSlug) # Input product slug
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[4]/section/div/span[2]/div/div/div/span[6]/div/div[2]/div/div[2]/button[1]").click() # Execute button
        time.sleep(180)

        driver.close()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
