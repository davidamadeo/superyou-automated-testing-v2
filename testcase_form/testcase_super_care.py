# Last tested 3/11/2021 14:21

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from decouple import config
import unittest, time, re

# Account Data
Email = config("EXISTING_USER_EMAIL", cast=str)
Password = config("EXISTING_USER_PASSWORD", cast=str)
MetodeKlaim = config("METODE_KLAIM", cast=str)

TglLahir = config("DAY_OF_BIRTH", cast=str)
BlnLahir = config("MONTH_OF_BIRTH", cast=str)
ThnLahir = config("YEAR_OF_BIRTH", cast=str)

 
class TestCaseSingleProduct(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(config("DRIVER_PATH", cast=str))
        # self.driver = webdriver.Chrome(config("DRIVER_PATH", cast=str))
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case_NewUser_SingleProduct(self):
        driver = self.driver
        driver.maximize_window() 
        driver.get("https://staging.superyou.co.id/") # Website Link
        time.sleep(1) # In Second

        # LOGIN PAGE #

        driver.find_element_by_id("masuk-button-header").click() # Login Button
        time.sleep(1)
        driver.find_element_by_id("user_email").click() # Email Field
        driver.find_element_by_id("user_email").send_keys(Email) # Email Field
        driver.find_element_by_id("user_password").click() # Password Field
        driver.find_element_by_id("user_password").send_keys(Password) # Password Field
        driver.find_element_by_id("login-button-loginpage").click() # Submit Button
        time.sleep(1)

        # Go to Home
        driver.find_element_by_id("superyou-logo-dashboard").click()
        time.sleep(2)

        # PRODUCT PAGE #

        # Go to Super Safe product page
        driver.find_element_by_id("produk-super-care-homepage").click() # Super Care Product Page Button
        time.sleep(1)
        driver.find_element_by_id("yuk-hitung-biaya-premi-product-page").click() # Yuk Hitung Biaya Premi button
        time.sleep(1)
        driver.find_element_by_id("pilih-plan-selectplan-product-page").click() 
        driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select Silver Plan dengan Santunan Tunai Harian COVID 19
        driver.find_element_by_id("tertanggung-selectplan-product-page").click()
        driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select Diri Sendiri 
        driver.find_element_by_id("insured_dob").click()
        driver.find_element_by_id("insured_dob").send_keys(TglLahir, BlnLahir, ThnLahir) # Input Date of Birth
        driver.find_element_by_id("kelamin-tertanggung-selectplan-product-page").click()
        driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select male

        if (MetodeKlaim) == 'reimbursement':
            driver.find_element_by_id("claim_method-11").click()
            time.sleep(5)

        elif (MetodeKlaim) == 'cashless':
            next

        driver.find_element_by_id("hitung-biaya-premi-selectplan-product-page").click() # Press Hitung Biaya Premi button
        time.sleep(1)

        # Click Bayar Sekarang
        driver.find_element_by_id("pay-now-selectplan-product-page").click() # Click Bayar Sekarang
        time.sleep(4)

        # FORM PAGE #

        time.sleep(5)
        element = []
        element = driver.find_elements_by_css_selector("#form-user .product-list .cart-item p")

        assert "Kamu hanya dapat memiliki 1 Polis Super Care Protection untuk 1 Tertanggung" in element[17].text

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