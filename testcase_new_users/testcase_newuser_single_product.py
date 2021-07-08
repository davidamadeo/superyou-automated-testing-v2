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

        if (Product) == "strong":
            # Go to Super Strong product page
            driver.find_element_by_xpath("/html/body/div[3]/header/div[4]/div/div/div[2]/div[1]/div[1]/div/div[3]/a").click() # Super Strong Product Page Button
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div/div[3]/div[1]/div/div/div/div[3]/a").click() # Pilih Plan Ini Button (Bronze Plan)
            time.sleep(1)
            driver.find_element_by_xpath("//input[@type='tel']").send_keys(TglLahir) # Input Date of Birth
            driver.find_element_by_xpath("(//input[@type='tel'])[2]").send_keys(BlnLahir) # Input Month
            driver.find_element_by_xpath("(//input[@type='tel'])[3]").send_keys(ThnLahir) # Input Year
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[3]/div[1]/section/div/div/div[2]/div[1]/div/div[3]/ul/li/div/a").click() # Click Beli Plan
            time.sleep(1)

        elif (Product) == "life":
            # Go to Super Life product page
            driver.find_element_by_xpath("/html/body/div[3]/header/div[4]/div/div/div[2]/div[1]/div[1]/div/div[2]/a").click() # Super Life Product Page Button
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[3]/div[1]/section[1]/div/div[3]/div[1]/div/div/div/div[3]/a").click() # Pilih Plan Ini Button (Bronze Plan)
            time.sleep(1)
            driver.find_element_by_xpath("//input[@type='tel']").send_keys(TglLahir) # Input Date of Birth
            driver.find_element_by_xpath("(//input[@type='tel'])[2]").send_keys(BlnLahir) # Input Month
            driver.find_element_by_xpath("(//input[@type='tel'])[3]").send_keys(ThnLahir) # Input Year
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[3]/div[1]/section[2]/div/div/div[2]/div[1]/div/div[3]/ul/li/div/a").click() #Click Beli Plan
            time.sleep(1)

        elif (Product) == "hospital":
            # Go to MyHospital product page
            driver.find_element_by_xpath("/html/body/div[3]/header/div[4]/div/div/div[2]/div[1]/div[1]/div/div[4]/a/img").click() # MyHospital Product Page Button
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[3]/div[5]/section[1]/div/div[3]/div[1]/div/div/div/div[3]/a").click() # Pilih Plan Ini Button (Bronze Plan)
            time.sleep(1)
            driver.find_element_by_xpath("//input[@type='tel']").send_keys(TglLahir) # Input Date of Birth
            driver.find_element_by_xpath("(//input[@type='tel'])[2]").send_keys(BlnLahir) # Input Month
            driver.find_element_by_xpath("(//input[@type='tel'])[3]").send_keys(ThnLahir) # Input Year
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[3]/div[5]/section[2]/div/div/div[2]/div[1]/div/div[3]/ul/li/div/a").click() # Click Beli Plan
            time.sleep(1)

        elif (Product) == "safe":
            # Go to Super Safe product page
            driver.find_element_by_xpath("/html/body/div[3]/header/div[4]/div/div/div[2]/div/div[1]/div/div[5]/a").click() # Super Safe Product Page Button
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div[3]/div[1]/section[1]/div/div[3]/div[1]/div/div/div/div[7]/a").click() # Click Plan Ini (Bronze Plan)
            time.sleep(1)
            driver.find_element_by_xpath("//input[@type='tel']").send_keys(TglLahir) # Input Date of Birth
            driver.find_element_by_xpath("(//input[@type='tel'])[2]").send_keys(BlnLahir) # Input Month
            driver.find_element_by_xpath("(//input[@type='tel'])[3]").send_keys(ThnLahir) # Input Year

            if (Riders) == 'holiday':
                # Pilih Rider
                driver.find_element_by_xpath("//section[@id='product-calculator']/div/div/div/div/div[5]/div/label").click() # Pilih Rider Super Holiday Protection

            elif (Riders) == 'motor':
                driver.find_element_by_xpath("//section[@id='product-calculator']/div/div/div/div/div[6]/div/label").click() # Pilih Rider SUper Motor Protection
            
            elif (Riders) == 'all':
                # Pilih Rider
                driver.find_element_by_xpath("//section[@id='product-calculator']/div/div/div/div/div[5]/div/label").click() # Pilih Rider Super Holiday Protection
                driver.find_element_by_xpath("//section[@id='product-calculator']/div/div/div/div/div[6]/div/label").click() # Pilih Rider SUper Motor Protection
            
            elif (Riders) == "null":
                next

            driver.find_element_by_xpath("/html/body/div[3]/div[1]/section[2]/div/div/div[2]/div[1]/div/div[3]/ul/li[3]/div/a").click() # Click Beli Plan
            time.sleep(1)

        elif (Product) == 'care': # With underwriting
            # Go to Super Care Product Page
            driver.find_element_by_link_text("Produk").click() # Click Produk dropdown
            driver.find_element_by_xpath("//div[@id='locale']/div[3]/div/div/div/div[2]/div[2]/div[7]/a/p").click()
            driver.find_element_by_xpath("/html/body/div/main/section[1]/section/div/div[1]/button").click() # Yuk Hitung Biaya Premi Kamu button
            driver.find_element_by_name("select-menu").click() # Pilih plan dropdown
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div/span").click() # Choose the plan
            time.sleep(1)
            driver.find_element_by_xpath("(//button[@name='select-menu'])[2]").click() # Tertanggung dropdown
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div/span").click() # Choose the insured
            time.sleep(1)
            driver.find_element_by_id("insured_dob").send_keys(TglLahir,"/",BlnLahir,"/",ThnLahir) # Input Date of Birth
            time.sleep(1)
            driver.find_element_by_xpath("(//button[@name='select-menu'])[3]").click() # Jenis kelamin tertanggung dropdown
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Choose gender
            time.sleep(1)
            driver.find_element_by_xpath("//div[@id='superyou']/main/section[4]/div/div/form/button").click() # Hitung biaya premi button
            time.sleep(1)
            driver.find_element_by_xpath("//div[@id='superyou']/main/section[4]/div/div/div/div/button").click() # Click tambah keranjang button
            time.sleep(1)

        elif (Product) == 'well':
            driver.find_element_by_xpath("/html/body/div/main/section[1]/section/div/div[1]/button").click() # Yuk Hitung Biaya Premi Kamu button
            driver.find_element_by_name("select-menu").click() # Pilih plan dropdown
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Choose the plan
            time.sleep(1)
            driver.find_element_by_xpath("(//button[@name='select-menu'])[2]").click() # Tertanggung dropdown
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Choose the insured
            time.sleep(1)
            driver.find_element_by_id("insured_dob").send_keys(TglLahir,"/",BlnLahir,"/",ThnLahir) # Input Date of Birth
            time.sleep(1)
            driver.find_element_by_xpath("(//button[@name='select-menu'])[3]").click() # Jenis kelamin tertanggung dropdown
            driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click() # Choose gender
            time.sleep(1)
            driver.find_element_by_xpath("//div[@id='superyou']/main/section[4]/div/div/form/button").click() # Hitung biaya premi button
            time.sleep(1)
            driver.find_element_by_xpath("/html/body/div/main/section[4]/div[1]/div/div/div/button[1]").click() # Click tambah keranjang button
            time.sleep(1)

        else:
            print("Wrong Input. Please input 'strong', 'safe', 'life', 'care', 'well' or 'hospital' in lower case letters.")

        # Click Tombol Keranjang
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/img").click() # Click Tombol Keranjang
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[5]/div/div[2]/div").click() # Click Lanjut Beli

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
        driver.find_element_by_xpath("//div[@id='form-user']/div[2]/div/div[3]/div/div[15]/button").click() # Click SUBMIT button
        time.sleep(1)

        if (Product) == 'strong' or 'safe' or 'life' or 'hospital':
            # Halaman Rincian Tertanggung
            driver.find_element_by_xpath("//div[@id='su-base-select']/div[2]/div/div").click() # Click Status Tertanggung
            driver.find_element_by_xpath("//div[@id='su-base-select']/div[2]/ul/li").click() # Select Tertanggung (Diri Sendiri)
            driver.find_element_by_xpath("/html/body/div/div[2]/div/div[4]/div/div[6]/button").click() # Lanjut Button (Halaman Rincian Tertanggung)
            time.sleep(1)

        elif (Product) == 'care' or 'well':
            # Halaman Rincian Tertanggung
            driver.find_element_by_xpath("//div[@id='su-base-select']/div[2]/div/div").click() #Click Status Tertanggung
            driver.find_element_by_xpath("//div[@id='su-base-select']/div[2]/ul/li").click() #Select Tertanggung (Diri Sendiri)
            driver.find_element_by_xpath("(//div[@id='su-base-select']/div/div)[4]").click() #Click Daftar Pekerjaan
            driver.find_element_by_xpath("//div[@id='su-base-select']/div/ul/li[16]").click() #Select Pekerjaan (Karyawan Swasta)
            driver.find_element_by_xpath("/html/body/div/div[2]/div/div[4]/div/div[7]/button").click() #Lanjut Button (Halaman Rincian Tertanggung)
            time.sleep(6)
            print("Nothing is happening")
            time.sleep(6)
            
            # Underwriting
            driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div[2]/div/div[1]/div[1]/div/label").click()
            driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div[2]/div/button").click()
            driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div[2]/div/div[1]/div[1]/div/label").click()
            driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div[2]/div/div[1]/div[1]/div/label").click()
            driver.find_element_by_xpath("//div[@id='base-radio-input']/div/div/label").click()
            driver.find_element_by_xpath("//div[@id='form-user']/div[4]/div/div/div[2]/div/button/span").click()
            driver.find_element_by_xpath("//div[@id='base-radio-input']/div/div/label").click()
            time.sleep(3)
            driver.find_element_by_xpath("//div[@id='form-user']/div[4]/div/div/div[2]/div/button").click()
            time.sleep(1)

        # Halaman Ahli Waris
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div/div[1]/div/div[2]/div").click() # Click Daftar Ahli Waris
        driver.find_element_by_xpath("//div[@id='su-base-select']/div[2]/ul/li[4]").click() # Select Daftar Ahli Waris
        driver.find_element_by_xpath("(//input[@name='name'])[3]").click()
        driver.find_element_by_xpath("(//input[@name='name'])[3]").send_keys(NamaAhliWaris) # Input Ahli Waris
        driver.find_element_by_xpath("(//input[@type='tel'])[11]").click()
        driver.find_element_by_xpath("(//input[@type='tel'])[11]").send_keys(TglLahirAhliWaris) # Input Beneficiary Date of Birth
        driver.find_element_by_xpath("(//input[@type='tel'])[12]").send_keys(BlnLahirAhliWaris) # Input Month of Beneficiary
        driver.find_element_by_xpath("(//input[@type='tel'])[13]").send_keys(ThnLahirAhliWaris) # Input Year of Beneficiary
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div/div[3]/div/div[1]/div/img").click() # Click Calendar Button
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div/div[3]/div/div[1]/div/img").click() # Click Calendar Button
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='form-user']/div[2]/div/div[5]/div/div[5]/button").click() # Submit Button (Halaman Rincian Tertanggung)
        time.sleep(1)

        # Input kode verifikasi Nomor Handphone
        driver.find_element_by_xpath("(//input[@type='tel'])[14]").click() # Input Handphone Verification Number = 321321
        driver.find_element_by_xpath("(//input[@type='tel'])[14]").send_keys("3")
        driver.find_element_by_xpath("(//input[@type='tel'])[15]").send_keys("2")
        driver.find_element_by_xpath("(//input[@type='tel'])[16]").send_keys("1")
        driver.find_element_by_xpath("(//input[@type='tel'])[17]").send_keys("3")
        driver.find_element_by_xpath("(//input[@type='tel'])[18]").send_keys("2")
        driver.find_element_by_xpath("(//input[@type='tel'])[19]").send_keys("1")
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click() # Submit Button (Halaman Konfirmasi Nomor HP)
        time.sleep(1)

        # Input Password
        driver.find_element_by_name("password").click()
        driver.find_element_by_name("password").send_keys(Password)
        driver.find_element_by_name("confirm_password").click()
        driver.find_element_by_name("confirm_password").send_keys(Password)
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(1)

        # Halaman pembayaran
        time.sleep(1)
        driver.find_element_by_xpath("//section[@id='sovia-payment']/form/div/div[2]/div[2]/div[2]/div/label").click() # Click S&K 1
        time.sleep(1)
        driver.find_element_by_xpath("//section[@id='sovia-payment']/form/div/div[2]/div[2]/div[3]/div/label").click() # Click S&K 2
        time.sleep(1)
        driver.find_element_by_xpath("//section[@id='sovia-payment']/form/div/div[2]/div[2]/div[4]/div/label").click() # Click S&K 3
        time.sleep(1)
        driver.find_element_by_xpath("//section[@id='sovia-payment']/form/div/div[2]/div[2]/div[5]/div/label").click() # Click S&K 4

        if (PaymentDuration) == 'yearly':
            driver.find_element_by_xpath("//div[@id='monthly-yearly']/div[2]/div[2]/label").click()

        else:
            next

        if (PaymentMethod) == "faspay":
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
            Select(driver.find_element_by_id("year")).select_by_visible_text("2021")
            driver.find_element_by_id("year").click()
            driver.find_element_by_name("submit").click() # Click Submit button
            time.sleep(2)
            driver.find_element_by_link_text("LIHAT AKUN KAMU").click()

        elif (PaymentMethod) == 'permata':
            driver.find_element_by_xpath("/html/body/section/form/div/div[2]/div[2]/div[8]/div/div/div/div[1]/div/div[3]/a/div").click()

        elif (PaymentMethod) == 'mandiri':
            driver.find_element_by_xpath("/html/body/section/form/div/div[2]/div[2]/div[8]/div/div/div/div[1]/div/div[2]/a/div").click()

        elif (PaymentMethod) == 'indomaret':
            driver.find_element_by_xpath("/html/body/section/form/div/div[2]/div[2]/div[8]/div/div/div/div[1]/div/div[4]/a/div").click()
            
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