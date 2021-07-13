# Last tested 3/11/2021 14:20

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
Email = config("NEW_USER_EMAIL", cast=str) # Unique
Phone = config("NEW_USER_PHONE", cast=str) # Unique

KTP = config("KTP", cast=str)
Password = config("NEW_USER_PASSWORD", cast=str)
Name = config("NAME", cast=str)
TglLahir = config("DAY_OF_BIRTH", cast=str)
BlnLahir = config("MONTH_OF_BIRTH", cast=str)
ThnLahir = config("YEAR_OF_BIRTH", cast=str)
Kelurahan = config("SUB_DISTRICT", cast=str)
Kota = config("CITY", cast=str)
TempatLahir = config("PLACE_OF_BIRTH", cast=str)
Alamat = config("ADDRESS", cast=str)
Kecamatan = config("DISTRICT", cast=str)
KodePos = config("POSTAL_CODE", cast=str)
NamaAhliWaris = config("NAME_BENEFICIARY", cast=str)
TglLahirAhliWaris = config("DAY_OF_BIRTH_BENEFICIARY", cast=str)
BlnLahirAhliWaris = config("MONTH_OF_BIRTH_BENEFICIARY", cast=str)
ThnLahirAhliWaris = config("YEAR_OF_BIRTH_BENEFICIARY", cast=str)

MetodeKlaim = config("METODE_KLAIM", cast=str)

Product = config("PRODUCT", cast=str)
PaymentMethod = config("PAYMENT_METHOD", cast=str)
Riders = config("RIDERS", cast=str)
PaymentDuration = config("PAYMENT_DURATION", cast=str)

CardName = config("CARD_NAME", cast=str)
CardNum = config("CARD_NUM", cast=str)
CardCVC = config("CARD_CVC", cast=str)
 
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
        time.sleep(1) #In Second 

        # PRODUCT PAGE #

        if (Product) == 'strong':
            # Go to Super Strong product page
            driver.find_element_by_id("produk-super-strong-homepage").click() # Super Strong Product Page Button
            time.sleep(1)
            driver.find_element_by_id("yuk-hitung-biaya-premi-product-page").click() # Yuk Hitung Biaya Premi button
            time.sleep(1)
            driver.find_element_by_id("pilih-plan-selectplan-product-page").click() 
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select Bronze Plan
            driver.find_element_by_id("tertanggung-selectplan-product-page").click()
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select Diri Sendiri 
            driver.find_element_by_id("insured_dob").click()
            driver.find_element_by_id("insured_dob").send_keys(TglLahir, BlnLahir, ThnLahir) # Input Date of Birth
            driver.find_element_by_id("kelamin-tertanggung-selectplan-product-page").click()
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select male
            driver.find_element_by_id("hitung-biaya-premi-selectplan-product-page").click() # Press Hitung Biaya Premi button
            time.sleep(1)

        elif (Product) == 'life':
            # Go to Super Life product page
            driver.find_element_by_id("produk-super-life-homepage").click() # Super Life Product Page Button
            time.sleep(1)
            driver.find_element_by_id("yuk-hitung-biaya-premi-product-page").click() # Yuk Hitung Biaya Premi button
            time.sleep(1)
            driver.find_element_by_id("pilih-plan-selectplan-product-page").click() 
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select Bronze Plan
            driver.find_element_by_id("tertanggung-selectplan-product-page").click()
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select Diri Sendiri 
            driver.find_element_by_id("insured_dob").click()
            driver.find_element_by_id("insured_dob").send_keys(TglLahir, BlnLahir, ThnLahir) # Input Date of Birth
            driver.find_element_by_id("kelamin-tertanggung-selectplan-product-page").click()
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select male
            driver.find_element_by_id("hitung-biaya-premi-selectplan-product-page").click() # Press Hitung Biaya Premi button
            time.sleep(1)
             
        elif (Product) == 'hospital':
            # Go to My Hospital product page
            driver.find_element_by_id("produk-my-hospital-homepage").click() # My Hospital Product Page Button
            time.sleep(1)
            driver.find_element_by_id("yuk-hitung-biaya-premi-product-page").click() # Yuk Hitung Biaya Premi button
            time.sleep(1)
            driver.find_element_by_id("pilih-plan-selectplan-product-page").click() 
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select Bronze Plan
            driver.find_element_by_id("tertanggung-selectplan-product-page").click()
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select Diri Sendiri 
            driver.find_element_by_id("insured_dob").click()
            driver.find_element_by_id("insured_dob").send_keys(TglLahir, BlnLahir, ThnLahir) # Input Date of Birth
            driver.find_element_by_id("kelamin-tertanggung-selectplan-product-page").click()
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select male
            driver.find_element_by_id("hitung-biaya-premi-selectplan-product-page").click() # Press Hitung Biaya Premi button
            time.sleep(1)

        elif (Product) == 'safe':
            # Go to Super Safe product page
            driver.find_element_by_id("produk-super-safe-homepage").click() # Super Safe Product Page Button
            time.sleep(1)
            driver.find_element_by_id("yuk-hitung-biaya-premi-product-page").click() # Yuk Hitung Biaya Premi button
            time.sleep(1)
            driver.find_element_by_id("pilih-plan-selectplan-product-page").click() 
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select Bronze Plan
            driver.find_element_by_id("tertanggung-selectplan-product-page").click()
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select Diri Sendiri 
            driver.find_element_by_id("insured_dob").click()
            driver.find_element_by_id("insured_dob").send_keys(TglLahir, BlnLahir, ThnLahir) # Input Date of Birth
            driver.find_element_by_id("kelamin-tertanggung-selectplan-product-page").click()
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select male

            if (Riders) == 'holiday':
                # Pilih Rider
                driver.find_element_by_id("select-rider0").click() # Pilih Rider Super Holiday Protection

            elif (Riders) == 'motor':
                driver.find_element_by_id("select-rider1").click() # Pilih Rider SUper Motor Protection
            
            elif (Riders) == 'all':
                # Pilih Rider
                driver.find_element_by_id("select-rider0").click() # Pilih Rider Super Holiday Protection
                driver.find_element_by_id("select-rider1").click() # Pilih Rider SUper Motor Protection
            
            elif (Riders) == 'null':
                next

            driver.find_element_by_id("hitung-biaya-premi-selectplan-product-page").click() # Press Hitung Biaya Premi button
            time.sleep(1)

        elif (Product) == 'care': 
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
                driver.find_element_by_id("claim_method-6").click()
                time.sleep(5)

            elif (MetodeKlaim) == 'cashless':
                next

            driver.find_element_by_id("hitung-biaya-premi-selectplan-product-page").click() # Press Hitung Biaya Premi button
            time.sleep(1)

        elif (Product) == 'well':
            driver.find_element_by_id("produk-super-well-homepage").click() # Super Well Product Page Button
            time.sleep(1)
            driver.find_element_by_id("yuk-hitung-biaya-premi-product-page").click() # Yuk Hitung Biaya Premi button
            time.sleep(1)
            driver.find_element_by_id("pilih-plan-selectplan-product-page").click() 
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select Gold Plan
            driver.find_element_by_id("tertanggung-selectplan-product-page").click()
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select Diri Sendiri 
            driver.find_element_by_id("insured_dob").click()
            driver.find_element_by_id("insured_dob").send_keys(TglLahir, BlnLahir, ThnLahir) # Input Date of Birth
            driver.find_element_by_id("kelamin-tertanggung-selectplan-product-page").click()
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Select male
            driver.find_element_by_id("hitung-biaya-premi-selectplan-product-page").click() # Press Hitung Biaya Premi button
            time.sleep(1)

        else:
            print("Wrong Input. Please input 'strong', 'safe', 'life' or 'hospital' in lower case letters.")

        # Click Bayar Sekarang
        driver.find_element_by_id("pay-now-selectplan-product-page").click() # Click Bayar Sekarang
        time.sleep(2)

        #Pengisi Form Isi Data
        time.sleep(3)
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").send_keys(Name) # Input Nama
        driver.find_element_by_xpath("//div[@id='form-user']/div[2]/div/div[3]/div/div[3]/div/div/div/label").click() # Select Gender: Male
        driver.find_element_by_name("citizen_id").click()
        driver.find_element_by_name("citizen_id").send_keys(KTP) # Input No. KTP (16 digits)
        driver.find_element_by_name("urban_district").click()
        driver.find_element_by_name("urban_district").send_keys(Kelurahan) # Input Kelurahan
        driver.find_element_by_name("city").click()
        driver.find_element_by_name("city").send_keys(Kota) # Input Kota
        driver.find_element_by_name("phone").click()
        driver.find_element_by_name("phone").send_keys(Phone) # Input No. Handphone
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").send_keys(Email) # Input Email
        driver.find_element_by_xpath("//input[@type='search']").click() # Click Status Pernikahan
        driver.find_element_by_xpath("//div[@id='su-base-select']/div/ul/li").click() # Select Status Pernikahan: Lajang
        driver.find_element_by_name("pob").click()
        driver.find_element_by_name("pob").send_keys(TempatLahir) # Input Tempat Lahir
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").send_keys(Alamat) # Input Alamat
        driver.find_element_by_name("sub_district").click()
        driver.find_element_by_name("sub_district").send_keys(Kecamatan) # Input Kecamatan
        driver.find_element_by_name("zip").click()
        driver.find_element_by_name("zip").send_keys(KodePos) # Input Kode Pos
        driver.find_element_by_xpath("(//div[@id='su-base-select']/div/div)[2]").click() # Click Daftar Pengeluaran
        driver.find_element_by_xpath("//div[@id='su-base-select']/div/ul/li[2]").click() # Select Daftar Pengeluaran (Rp3jt - 6jt)
        time.sleep(2)
        driver.find_element_by_name("lanjut_button").click() # Click Button SUBMIT
        time.sleep(1)

        if (Product) == 'strong' or 'safe' or 'life' or 'hospital':
            # Halaman Rincian Tertanggung
            driver.find_element_by_css_selector(".form__insured .btn-wrapper button[name='lanjut_button']").click() # Lanjut Button (Halaman Rincian Tertanggung)
            time.sleep(1)

        if (Product) == 'care':
            # First question UW
            driver.find_element_by_css_selector(".iwsMrY .vs__selected-options input[class='vs__search']").click()
            driver.find_element_by_xpath("//div[@id='su-base-select']/div/ul/li").click()
            driver.find_element_by_id("lanjut-button").click()

            # Second question UW
            element = driver.find_element_by_css_selector("#base-radio-input .radio [for='yesno-1']")
            driver.execute_script("arguments[0].click();", element) 
            
            time.sleep(1)

            element = driver.find_element_by_id("lanjut-button")
            driver.execute_script("arguments[0].click();", element) 

            time.sleep(1)


            # Third question UW
            element = driver.find_element_by_css_selector("#base-radio-input .radio [for='yesno-1']")
            driver.execute_script("arguments[0].click();", element) 
            
            time.sleep(1)

            element = driver.find_element_by_id("lanjut-button")
            driver.execute_script("arguments[0].click();", element) 

            time.sleep(1)

            element_button = driver.find_element_by_class_name("fJqyJl")
            driver.execute_script("arguments[0].click();", element_button) 

            time.sleep(1)

        if (Product) == 'well':
            # First question UW
            element = driver.find_element_by_css_selector("#base-radio-input .radio [for='yesno-1']")
            driver.execute_script("arguments[0].click();", element) 

            time.sleep(1)

            driver.find_element_by_id("lanjut-button").click()

            # Second question UW
            element = driver.find_element_by_css_selector("#base-radio-input .radio [for='yesno-0']")
            driver.execute_script("arguments[0].click();", element) 
            
            time.sleep(1)

            element = driver.find_element_by_id("lanjut-button")
            driver.execute_script("arguments[0].click();", element) 

            time.sleep(1)


            # Third question UW
            element = driver.find_element_by_css_selector("#base-radio-input .radio [for='yesno-0']")
            driver.execute_script("arguments[0].click();", element) 
            
            time.sleep(1)

            element = driver.find_element_by_id("lanjut-button")
            driver.execute_script("arguments[0].click();", element) 

            time.sleep(1)

            element_button = driver.find_element_by_class_name("fJqyJl")
            driver.execute_script("arguments[0].click();", element_button) 

            time.sleep(1)

        # Halaman Ahli Waris
        driver.find_element_by_css_selector(".form__beneficiary .each-field input[class='vs__search']").click() # Click Daftar Ahli Waris
        driver.find_element_by_xpath("//div[@id='su-base-select']/div[2]/ul/li").click() # Select Daftar Ahli Waris
        driver.find_element_by_css_selector(".form__beneficiary .each-field input[name='name']").click()
        driver.find_element_by_css_selector(".form__beneficiary .each-field input[name='name']").send_keys(NamaAhliWaris)
        driver.find_element_by_css_selector(".form__beneficiary .each-field input[placeholder='dd']").click()
        driver.find_element_by_css_selector(".form__beneficiary .each-field input[placeholder='dd']").send_keys(TglLahir) # Input Date of Birth of Beneficiary
        driver.find_element_by_css_selector(".form__beneficiary .each-field input[placeholder='mm']").send_keys(BlnLahirAhliWaris) # Input Month of Beneficiary
        driver.find_element_by_css_selector(".form__beneficiary .each-field input[placeholder='yyyy']").send_keys(ThnLahirAhliWaris) # Input Year of Beneficiary
        time.sleep(1)
        driver.find_element_by_id("lanjut_button").click() # Submit Button (Halaman Rincian Tertanggung)

        # VERIFIKASI NEW USER #

        # Input kode verifikasi Nomor Handphone
        driver.find_element_by_css_selector(".e-modals .modal-content [class='verification__security-code-field']:nth-child(1) input").click() # Input Handphone Verification Number = 321321
        driver.find_element_by_css_selector(".e-modals .modal-content [class='verification__security-code-field']:nth-child(1) input").send_keys("3")
        driver.find_element_by_css_selector(".e-modals .modal-content [class='verification__security-code-field']:nth-child(2) input").send_keys("2")
        driver.find_element_by_css_selector(".e-modals .modal-content [class='verification__security-code-field']:nth-child(3) input").send_keys("1")
        driver.find_element_by_css_selector(".e-modals .modal-content [class='verification__security-code-field']:nth-child(4) input").send_keys("3")
        driver.find_element_by_css_selector(".e-modals .modal-content [class='verification__security-code-field']:nth-child(5) input").send_keys("2")
        driver.find_element_by_css_selector(".e-modals .modal-content [class='verification__security-code-field']:nth-child(6) input").send_keys("1")
        time.sleep(1)
        driver.find_element_by_id("verifikasi-submit-button-form").click() # Submit Button (Halaman Konfirmasi Nomor HP)
        time.sleep(1)

        # Input Password
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").send_keys(Password)
        driver.find_element_by_name("confirm_password").click()
        driver.find_element_by_name("confirm_password").send_keys(Password)
        time.sleep(1)
        driver.find_element_by_id("password-submit-button-form").click()
        time.sleep(1)

        # SUMMARY PAGE #

        # Halaman pembayaran
        time.sleep(1)
        driver.find_element_by_id("tnc1").click() # Click S&K 1
        time.sleep(1)
        driver.find_element_by_id("tnc2").click() # Click S&K 2
        time.sleep(1)
        driver.find_element_by_id("tnc3").click() # Click S&K 3
        time.sleep(1)
        driver.find_element_by_id("tnc4").click() # Click S&K 4

        if (PaymentDuration) == 'yearly':
            driver.find_element_by_css_selector(".n_content .payment-type .custom-radio-checkbox [for='radioYearly']").click()

        else:
            next

        if (PaymentMethod) == 'faspay':
            # Pilih metode pembayaran
            driver.find_element_by_id("next-step").click() # SUBMIT

            # Halaman Faspay
            driver.find_element_by_name("CARDNAME").click()
            driver.find_element_by_name("CARDNAME").send_keys(CardName) # Input Card Name
            driver.find_element_by_name("CARDTYPE").click()
            driver.find_element_by_id("CARDNOSHOWFORMAT").click()
            driver.find_element_by_id("CARDNOSHOWFORMAT").send_keys(CardNum) # Input Card Number
            driver.find_element_by_name("CARDCVC").click()
            driver.find_element_by_name("CARDCVC").send_keys(CardCVC) # Input CVC
            driver.find_element_by_id("month").click()
            Select(driver.find_element_by_id("month")).select_by_visible_text("May")
            driver.find_element_by_id("month").click()
            driver.find_element_by_id("year").click()
            Select(driver.find_element_by_id("year")).select_by_visible_text("2022")
            driver.find_element_by_id("year").click()
            driver.find_element_by_name("submit").click() # Click Submit button
            time.sleep(2)
            driver.find_element_by_link_text("LIHAT AKUN KAMU").click()

        elif (PaymentMethod) == 'mandiri':
            # Pilih metode pembayaran
            driver.find_element_by_css_selector(".n_content .l-payment .payment-list [data-value='12']").click()
            driver.find_element_by_id("next-step").click() # SUBMIT
            
            # Cek status pembayaran
            driver.find_element_by_id("cek-status-pembayaran").click() # Check payment status

        elif (PaymentMethod) == 'permata':
            # Pilih metode pembayaran
            driver.find_element_by_css_selector(".n_content .l-payment .payment-list [data-value='14']").click()
            driver.find_element_by_id("next-step").click() # SUBMIT

            # Cek status pembayaran
            driver.find_element_by_id("cek-status-pembayaran").click() # Check payment status

        elif (PaymentMethod) == 'indomaret':
            # Pilih metode pembayaran
            driver.find_element_by_css_selector(".n_content .l-payment .payment-list [data-value='19']").click()
            driver.find_element_by_id("next-step").click() # SUBMIT
            
            # Cek status pembayaran
            driver.find_element_by_id("cek-status-pembayaran").click() # Check payment status

        elif (PaymentMethod) == 'gopay':
            # Pilih metode pembayaran
            driver.find_element_by_css_selector(".n_content .l-payment .payment-list [data-value='22']").click()
            driver.find_element_by_id("next-step").click() # SUBMIT
            
            # Cek status pembayaran
            driver.find_element_by_id("cek-status-pembayaran").click() # Check payment status
            
        else:
            print("Wrong Input. Please input 'faspay', 'mandiri', 'permata' or 'indomaret' in lower case letters.")
        
        time.sleep(6)
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