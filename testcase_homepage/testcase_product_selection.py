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

        driver.execute_script("window.scrollTo(0, 780)") # Scroll to Product Selection
        time.sleep(3)

        element = driver.find_elements_by_id("other-products-price-my-hospital")

        assert "Rp 39.500" in element[0].text

        element = []
        element = driver.find_elements_by_id("other-products-price-super-life")

        assert "Rp 33.000" in element[0].text

        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        element = []
        element = driver.find_elements_by_id("other-products-price-super-strong")

        assert "Rp 28.500" in element[0].text

        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        element = []
        element = driver.find_elements_by_id("other-products-price-super-care")

        assert "Rp 45.000" in element[0].text

        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        element = []
        element = driver.find_elements_by_id("other-products-price-super-safe")

        assert "Rp 36.500" in element[0].text

        driver.find_element_by_css_selector("#superyou .other-products__wrapper button[aria-label='Next']").click()
        element = []
        element = driver.find_elements_by_id("other-products-price-super-well")

        assert "Rp 50.000" in element[0].text

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