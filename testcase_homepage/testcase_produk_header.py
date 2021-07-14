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

        time.sleep(3)

        driver.find_element_by_id("produk-dropdown-header").click()

        element = driver.find_elements_by_css_selector("#superyou .products__ddown [href='/produk/super-life-protection'] .meta-desc")

        assert "Mulai dari Rp 33.000/Bulan" in element[0].text
        element = []

        element = driver.find_elements_by_css_selector("#superyou .products__ddown [href='/produk/super-safe-protection'] .meta-desc")

        assert "Mulai dari Rp 36.500/Bulan" in element[0].text
        element = []

        element = driver.find_elements_by_css_selector("#superyou .products__ddown #produk-super-motor-header .meta-desc")

        assert "Tambahan Mulai dari Rp 9.500/Bulan" in element[0].text
        element = []

        element = driver.find_elements_by_css_selector("#superyou .products__ddown #produk-super-holiday-header .meta-desc")

        assert "Tambahan Mulai dari Rp 21.000/Bulan" in element[0].text
        element = []

        element = driver.find_elements_by_css_selector("#superyou .products__ddown [href='/produk/my-hospital-protection'] .meta-desc")

        assert "Mulai Dari Rp 39.500/Bulan" in element[0].text
        element = []

        element = driver.find_elements_by_css_selector("#superyou .products__ddown [href='/produk/super-well-protection'] .meta-desc")

        assert "Mulai Dari Rp 50.000/Bulan" in element[0].text
        element = []

        element = driver.find_elements_by_css_selector("#superyou .products__ddown [href='/produk/super-care-protection'] .meta-desc")

        assert "Mulai Dari Rp 45.000/Bulan" in element[0].text
        element = []

        element = driver.find_elements_by_css_selector("#superyou .products__ddown [href='/produk/super-strong-protection'] .meta-desc")

        assert "Mulai dari Rp 28.500/Bulan" in element[0].text

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