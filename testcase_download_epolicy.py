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

class TestCaseLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(PATH)
        # self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case_login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://staging.superyou.co.id/") #Link Website
        time.sleep(1) #In Second
        driver.find_element_by_xpath("/html/body/div[3]/header/div[1]/div[3]/div/div/div[2]/a[2]").click() #Login Button
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/header/div[1]/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[1]/input").click() #Email Column
        time.sleep(0.5)
        Email = driver.find_element_by_xpath("/html/body/div[3]/header/div[1]/div[2]/div/div/div/div[2]/div/div/form/div[1]/div[1]/input") #Email Column
        Email.send_keys("John@doe.com") #Input Email
        time.sleep(1)
        driver.find_element_by_id("password").click() #Password Column
        time.sleep(0.5)
        Password = driver.find_element_by_id("password") #Password Column
        Password.send_keys("john@doe") #Input Password 
        time.sleep(1)
        driver.find_element_by_id("submit_login").click() #Submit Button
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[3]/ul/li[1]/a").click() #E-Policy Page
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/div[5]/div/div/div/div[2]/div[1]/a").click() #Download E-Policy
        time.sleep(7)
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