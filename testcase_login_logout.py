# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re

# For Microsoft Edge Users
PATH = "C:/msedgedriver.exe"

# For Chrome Users
# PATH = "C:/chromedriver.exe"

# Variables
Email = "john@doe.com"
Password = "john@doe"


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(PATH)
        # self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://staging.superyou.co.id/id")
        driver.find_element_by_xpath(
            "/html/body/div[3]/header/div[1]/div[3]/div/div/div[2]/a[2]").click()
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(Email)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(Password)
        driver.find_element_by_id("form-login").submit()
        driver.find_element_by_xpath(
            "//div[2]/div/div/div/div/a/div[2]").click()
        driver.find_element_by_xpath("//a[2]/span").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
