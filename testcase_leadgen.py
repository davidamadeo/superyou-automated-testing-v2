# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

# For Microsoft Edge Users
PATH = "C:/msedgedriver.exe"

# For Chrome Users
# PATH = "C:/chromedriver.exe"

Name = "John Doe"
Handphone = "0812345678777"
Email = "johndoe777@gmail.com"

class TestLeadGen(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(PATH)
        # self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case_LeadGen(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://staging.superyou.co.id/") #Link Website
        time.sleep(1) #In Second
        driver.find_element_by_id("Nama").click()
        driver.find_element_by_id("Nama").send_keys(Name)
        driver.find_element_by_id("Handphone").click()
        driver.find_element_by_id("Handphone").send_keys(Handphone)
        driver.find_element_by_id("Email").click()
        driver.find_element_by_id("Email").send_keys(Email)
        driver.find_element_by_xpath("//div[@id='super-lead']/div/div/div/div[2]/div/form/button").click()
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

# Link dokumentasi Python Selenium:
# https://selenium-python.readthedocs.io/api.html

# Steps untuk jalankan Automation Test:

# 1. Install Python:
# https://www.python.org/downloads/

# 2. Install Selenium melalui code ini pada Terminal:
# - Windows: pip install Selenium
# - Mac: pip3 install Selenium

# 3. WAJIB download chromedriver di link https://sites.google.com/a/chromium.org/chromedriver/home
# Sesuaikan versi chromedriver dengan versi Browser Chrome yang dimiliki saat ini
# Masukkan path file driver hasil download pada PATH di atas (PATH = "C:\chromedriver.exe")

# 4. Beberapa cara run automation test:
# - Visual Code: Tekan Button Play (Pojok Kanan Atas)
# - Terminal (Windows): Ketik "python Test_Case_Login.py" lalu tekan Enter
# - Terminal (Mac): Ketik "python3 Test_Case_Login.py" lalu tekan Enter