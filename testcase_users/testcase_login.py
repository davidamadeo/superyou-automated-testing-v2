# Last tested 3/11/2021 14:15

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from decouple import config
import unittest, time, re

Email = config("EXISTING_USER_EMAIL", cast=str)
Password = config("EXISTING_USER_PASSWORD", cast=str)
Page = config("DASHBOARD_PAGE", cast=str)

class TestCaseLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(config("DRIVER_PATH", cast=str))
        # self.driver = webdriver.Chrome(config("DRIVER_PATH", cast=str))
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://staging.superyou.co.id/") # Website Link

        # LOGIN PAGE #

        driver.find_element_by_id("masuk-button-header").click() # Login Button
        time.sleep(1)
        driver.find_element_by_id("user_email").click() # Email Field
        driver.find_element_by_id("user_email").send_keys(Email) # Email Field
        driver.find_element_by_id("user_password").click() # Password Field
        driver.find_element_by_id("user_password").send_keys(Password) # Password Field
        driver.find_element_by_id("login-button-loginpage").click() # Submit Button
        time.sleep(1)
        
        if (Page) == "e-policy":
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/ul/li[1]/a").click() # E-Policy Page
            time.sleep(3)

        elif (Page) == "claim":
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/ul/li[2]/a").click() # Claim Page
            time.sleep(3)

        elif (Page) == "payment":
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/ul/li[3]/a").click() # Payment Page
            time.sleep(3)

        elif (Page) == "all":
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/ul/li[1]/a").click() # E-Policy Page
            time.sleep(3)
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/ul/li[2]/a").click() # Claim Page
            time.sleep(3)
            driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/ul/li[3]/a").click() # Payment Page
            time.sleep(3)

        else:
            print("Wrong Input. Please input 'e-policy', 'claim', 'payment' or 'all' in lower case letters.")

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