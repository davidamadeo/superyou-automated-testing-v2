# Last tested 3/12/2021 14:20

# NOTES: DO NOT FORGET TO EDIT THE JSON REQUEST BODY ON LINE 50

# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from decouple import config
import unittest, time, re

Username = config("DOCS_USERNAME", cast=str)
Password = config("DOCS_PASSWORD", cast=str)

class UntitledTestCase8(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(config("DRIVER_PATH", cast=str))
        # self.driver = webdriver.Chrome(config("DRIVER_PATH", cast=str))
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case8(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://staging-underwriting.superyou.co.id/docs") # Website Link
        time.sleep(1)

        # Login
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/section/div/button").click() # Click Authroize Button
        driver.find_element_by_id("oauth_username").click() # Click username field
        driver.find_element_by_id("oauth_username").clear()
        driver.find_element_by_id("oauth_username").send_keys(Username) # Enter username
        driver.find_element_by_id("oauth_password").clear()
        driver.find_element_by_id("oauth_password").send_keys(Password) # Enter password
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/section/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[4]/button[1]").click() # Click authorize
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/section/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[3]/button[2]").click() # Click close
        time.sleep(2)
        
        # Execute process
        driver.find_element_by_xpath("//div[@id='operations-scorings-create_scoring_for_user_api_v1_scorings__post']/div").click() # POST method for new scoring
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[4]/section/div/span[8]/div/div/span/div/div[2]/div/div[1]/div[1]/div[2]/button").click() # Try it out button
        driver.find_element_by_xpath("//div[@id='swagger-ui']/div/div[2]/div[4]").click()
        driver.find_element_by_xpath("//div[@id='operations-scorings-create_scoring_for_user_api_v1_scorings__post']/div[2]/div/div/div[3]/div[2]/div/div/div/textarea").clear() # Clear default request body
        driver.find_element_by_xpath("//div[@id='operations-scorings-create_scoring_for_user_api_v1_scorings__post']/div[2]/div/div/div[3]/div[2]/div/div/div/textarea").send_keys("""
        {
                "products": [
                {
                        "product_code":"DSS1",
                        "product_plan_code":"bronze-plan"
                    }
                ],
                "answered_questions": {
                    "question_id": "string",
                    "form_field": "string",
                    "question_no": 0,
                    "answers": [
                    {
                        "answer_text": "string",
                        "question_id": "string",
                        "id": "string"
                    }
                    ]
                },
                "transaction_id": "string"
        }
        """) # Input request body
        driver.find_element_by_xpath("/html/body/div/div/div[2]/div[4]/section/div/span[8]/div/div/span/div/div[2]/div/div[2]/button[1]").click() # Execute button
        time.sleep(60)

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
