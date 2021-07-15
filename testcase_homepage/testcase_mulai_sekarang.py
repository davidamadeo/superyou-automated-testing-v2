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

TglLahirMin = config("DAY_OF_BIRTH_MIN", cast=str)
BlnLahirMin = config("MONTH_OF_BIRTH_MIN", cast=str)
ThnLahirMin = config("YEAR_OF_BIRTH_MIN", cast=str)

TglLahirMax = config("DAY_OF_BIRTH_MAX", cast=str)
BlnLahirMax = config("MONTH_OF_BIRTH_MAX", cast=str)
ThnLahirMax = config("YEAR_OF_BIRTH_MAX", cast=str)

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

        driver.find_element_by_id("mulai-sekarang-homepage").click() # Mulai Sekarang Button at homepage
        driver.find_element_by_css_selector(".welcome-container .su-date-wrapper input[placeholder='dd']").click()
        driver.find_element_by_css_selector(".welcome-container .su-date-wrapper input[placeholder='dd']").send_keys(TglLahirMax)
        driver.find_element_by_css_selector(".welcome-container .su-date-wrapper input[placeholder='mm']").send_keys(BlnLahirMax)
        driver.find_element_by_css_selector(".welcome-container .su-date-wrapper input[placeholder='yyyy']").send_keys(ThnLahirMax)

        driver.find_element_by_css_selector(".welcome-container button[type='submit']").click()

        assert "Batas usia maksimal 100 tahun" in driver.page_source
        time.sleep(2)

        driver.refresh()
        time.sleep(2)

        driver.find_element_by_css_selector(".welcome-container .su-date-wrapper input[placeholder='dd']").click()
        driver.find_element_by_css_selector(".welcome-container .su-date-wrapper input[placeholder='dd']").send_keys(TglLahirMin)
        driver.find_element_by_css_selector(".welcome-container .su-date-wrapper input[placeholder='mm']").send_keys(BlnLahirMin)
        driver.find_element_by_css_selector(".welcome-container .su-date-wrapper input[placeholder='yyyy']").send_keys(ThnLahirMin)

        driver.find_element_by_css_selector(".welcome-container button[type='submit']").click()

        assert "Usia masuk minimal 17 tahun (Tertanggung menjadi pemegang polis)" in driver.page_source
        time.sleep(2)
        
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