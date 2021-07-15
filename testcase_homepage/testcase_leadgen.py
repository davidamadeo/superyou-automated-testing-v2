# Last tested 3/11/2021 14:14

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from decouple import config
import unittest, time, re

Name = config("EXISTING_USER_NAME", cast=str)
Handphone = config("EXISTING_USER_PHONE", cast=str)
Email = config("EXISTING_USER_EMAIL", cast=str)

class TestLeadGen(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(config("DRIVER_PATH", cast=str))
        # self.driver = webdriver.Chrome(config("DRIVER_PATH", cast=str))
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case_LeadGen(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://staging.superyou.co.id/") #Link Website
        time.sleep(1) #In Second

        driver.execute_script("window.scrollTo(0, 1600)") # Scroll to Leadgen

        driver.find_element_by_id("Nama").click() # Name Field
        driver.find_element_by_id("Nama").send_keys(Name) # Input Name
        driver.find_element_by_id("Handphone").click() # Phone Field
        driver.find_element_by_id("Handphone").send_keys(Handphone) # Input Phone Num
        driver.find_element_by_id("Email").click() # Email Field
        driver.find_element_by_id("Email").send_keys(Email) # Input Email
        driver.find_element_by_css_selector("#superyou .leadgen-container button").click() # Hubungi Saya button
        time.sleep(3)

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