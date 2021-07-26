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
        time.sleep(1) # In Second
        
        # PRODUCT FROM HEADER #

        driver.find_element_by_id("produk-dropdown-header").click()        
        driver.find_element_by_id("produk-super-life-header").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-dropdown-header").click()
        driver.find_element_by_id("produk-super-safe-header").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-dropdown-header").click()
        driver.find_element_by_id("produk-super-motor-header").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-dropdown-header").click()
        driver.find_element_by_id("produk-super-holiday-header").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-dropdown-header").click()
        driver.find_element_by_id("produk-my-hospital-header").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-dropdown-header").click()
        driver.find_element_by_id("produk-super-well-header").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-dropdown-header").click()
        driver.find_element_by_id("produk-super-care-header").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-dropdown-header").click()
        driver.find_element_by_id("produk-super-strong-header").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        # PRODUCT FROM HOMEPAGE #

        driver.find_element_by_id("produk-super-life-homepage").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-super-safe-homepage").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-super-motor-homepage").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-super-holiday-homepage").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-my-hospital-homepage").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-super-well-homepage").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-super-care-homepage").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.find_element_by_id("produk-super-strong-homepage").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        # FROM PRODUCT SELECTION #

        driver.execute_script("window.scrollTo(0, 780)") # Scroll to Product Selection
        time.sleep(1)
        driver.find_element_by_id("other-products-detail-super-life").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 780)") # Scroll to Product Selection
        time.sleep(1)
        driver.find_element_by_id("other-products-detail-super-strong").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 780)") # Scroll to Product Selection
        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        time.sleep(1)
        driver.find_element_by_id("other-products-detail-super-care").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 780)") # Scroll to Product Selection
        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        time.sleep(1)
        driver.find_element_by_id("other-products-detail-super-safe").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 780)") # Scroll to Product Selection
        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        time.sleep(1)
        driver.find_element_by_id("other-products-detail-super-well").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 780)") # Scroll to Product Selection
        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        time.sleep(1)
        driver.find_element_by_id("other-products-detail-my-hospital").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        # PRODUK FROM FOOTER #
      
        driver.execute_script("window.scrollTo(0, 3500)") # Scroll to footer
        time.sleep(1)
        driver.find_element_by_id("produk-super-life-footer").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 3500)") # Scroll to footer
        time.sleep(1)
        driver.find_element_by_id("produk-super-safe-footer").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 3500)") # Scroll to footer
        time.sleep(1)
        driver.find_element_by_id("produk-super-motor -footer").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 3500)") # Scroll to footer
        time.sleep(1)
        driver.find_element_by_id("produk-super-holiday-footer").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 3500)") # Scroll to footer
        time.sleep(1)
        driver.find_element_by_id("produk-my-hospital-footer").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 3500)") # Scroll to footer
        time.sleep(1)
        driver.find_element_by_id("produk-super-well-footer").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 3500)") # Scroll to footer
        time.sleep(1)
        driver.find_element_by_id("produk-super-care-footer").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

        driver.execute_script("window.scrollTo(0, 3500)") # Scroll to footer
        time.sleep(1)
        driver.find_element_by_id("produk-super-strong-footer").click()
        driver.find_element_by_id("superyou-logo-header").click()
        time.sleep(1)

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