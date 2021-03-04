# Underwriting still not working

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

Email = "smith0003@email.com" # Wajib Unik
Phone = "081234567985" # Wajib Unik

KTP = "1234567890123966"
Password = "Abcd1234"
Name = "John Doe"
TglLahir = "01"
BlnLahir = "01"
ThnLahir = "1991"
Kelurahan = "Kelurahan"
Kota = "Jakarta"
TempatLahir = "Jakarta"
Alamat = "Jl. Jakarta No. 1"
Kecamatan = "Kecamatan"
KodePos = "12345"
NamaAhliWaris = "Jane Doe"
TglLahirAhliWaris = "02"
BlnLahirAhliWaris = "02"
ThnLahirAhliWaris = "1992"

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
        driver.maximize_window()
        driver.get("https://staging.superyou.co.id/") # Link Website
        time.sleep(1) # In Seconds

        # Go to Super Care Product Page
        driver.find_element_by_link_text("Produk").click()
        driver.find_element_by_xpath("//div[@id='locale']/div[3]/div/div/div/div[2]/div[2]/div[7]/a/p").click()
        driver.find_element_by_xpath("/html/body/div/main/section[1]/section/div/div[1]/button").click()
        driver.find_element_by_name("select-menu").click()
        driver.find_element_by_xpath("//li[@id='listbox-item-0']/div/span").click()
        # time.sleep(1)
        driver.find_element_by_xpath("(//button[@name='select-menu'])[2]").click()
        driver.find_element_by_xpath("//li[@id='listbox-item-0']/div/span").click()
        # time.sleep(1)
        driver.find_element_by_id("insured_dob").send_keys(TglLahir,"/",BlnLahir,"/",ThnLahir)
        # time.sleep(1)
        driver.find_element_by_xpath("(//button[@name='select-menu'])[3]").click()
        driver.find_element_by_xpath("//li[@id='listbox-item-0']/div").click()
        # time.sleep(1)

        # Tambah Produk ke Keranjang
        driver.find_element_by_xpath("//div[@id='superyou']/main/section[4]/div/div/form/button").click()
        # time.sleep(1)
        driver.find_element_by_xpath("//div[@id='superyou']/main/section[4]/div/div/div/div/button").click()

        # Klik Tombol Keranjang
        # time.sleep(1)
        driver.find_element_by_xpath("//img[@alt='Keranjang Belanja Super You']").click() # Klik Tombol Keranjang
        driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[3]/button").click() # Klik Lanjut Beli
        
        # Pengisi Form Isi Data
        time.sleep(3)
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").send_keys(Name) # Input Nama
        driver.find_element_by_xpath("//div[@id='form-user']/div[2]/div/div[3]/div/div[3]/div/div/div/label").click() # Select Gender: Male
        driver.find_element_by_name("citizen_id").click()
        driver.find_element_by_name("citizen_id").send_keys(KTP) #Input No. KTP (16 digits)
        driver.find_element_by_name("urban_district").click()
        driver.find_element_by_name("urban_district").send_keys(Kelurahan) #Input Kelurahan
        driver.find_element_by_name("city").click()
        driver.find_element_by_name("city").send_keys(Kota) #Input Kota
        driver.find_element_by_name("phone").click()
        driver.find_element_by_name("phone").send_keys(Phone) #Input No. Handphone
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").send_keys(Email)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div[4]/div/div/div/div[1]").click() #Click Status Pernikahan
        driver.find_element_by_xpath("//div[@id='su-base-select']/div/ul/li").click() #Select Status Pernikahan: Lajang
        driver.find_element_by_name("pob").click()
        driver.find_element_by_name("pob").send_keys(TempatLahir) #Input Tempat Lahir
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").send_keys(Alamat) #Input Alamat
        driver.find_element_by_name("sub_district").click()
        driver.find_element_by_name("sub_district").send_keys(Kecamatan) #Input Kecamatan
        driver.find_element_by_name("zip").click()
        driver.find_element_by_name("zip").send_keys(KodePos) #Input Kode Pos
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div[14]/div/div/div/div[1]").click() #Click Daftar Pengeluaran
        driver.find_element_by_xpath("//div[@id='su-base-select']/div/ul/li[2]").click() #Select Daftar Pengeluaran (Rp3jt - 6jt)
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div[15]/button").click()
        time.sleep(1)

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
        # driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div[2]/div/div[1]/div[1]/div/label").click()
        # driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div[2]/div/button").click()
        # driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div[2]/div/div[1]/div[1]/div/label").click()
        # driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div[2]/div/div[1]/div[1]/div/label").click()
        # driver.find_element_by_xpath("//div[@id='base-radio-input']/div/div/label").click()
        # driver.find_element_by_xpath("//div[@id='form-user']/div[4]/div/div/div[2]/div/button/span").click()
        # driver.find_element_by_xpath("//div[@id='base-radio-input']/div/div/label").click()
        # time.sleep(3)
        # driver.find_element_by_xpath("//div[@id='form-user']/div[4]/div/div/div[2]/div/button").click()
        # time.sleep(1)

        # Halaman Ahli Waris
        driver.find_element_by_xpath("(//input[@type='search'])[5]").click() #Click Daftar Ahli Waris
        driver.find_element_by_xpath("//div[@id='su-base-select']/div[2]/ul/li[4]").click() #Select Daftar Ahli Waris
        driver.find_element_by_xpath("(//input[@name='name'])[3]").click()
        driver.find_element_by_xpath("(//input[@name='name'])[3]").send_keys(NamaAhliWaris) #Input Ahli Waris
        driver.find_element_by_xpath("(//input[@type='tel'])[11]").click()
        driver.find_element_by_xpath("(//input[@type='tel'])").send_keys(TglLahirAhliWaris,"/",BlnLahirAhliWaris,"/",ThnLahirAhliWaris)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div/div[3]/div/div[1]/div/img").click() #Click Calendar Button
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div/div[3]/div/div[1]/div/img").click() #Click Calendar Button
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div/div[5]/button").click() #Submit Button (Halaman Rincian Tertanggung)
        time.sleep(1)

        # Input kode verifikasi Nomor Handphone
        driver.find_element_by_xpath("(//input[@type='tel'])[14]").click() #Input nomor verfikasi Handphone = 321321
        driver.find_element_by_xpath("(//input[@type='tel'])[14]").send_keys("3")
        driver.find_element_by_xpath("(//input[@type='tel'])[15]").send_keys("2")
        driver.find_element_by_xpath("(//input[@type='tel'])[16]").send_keys("1")
        driver.find_element_by_xpath("(//input[@type='tel'])[17]").send_keys("3")
        driver.find_element_by_xpath("(//input[@type='tel'])[18]").send_keys("2")
        driver.find_element_by_xpath("(//input[@type='tel'])[19]").send_keys("1")
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click() #Submit Button (Halaman Konfirmasi Nomor HP)
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
        driver.find_element_by_xpath("//section[@id='sovia-payment']/form/div/div[2]/div[2]/div[2]/div/label").click() #Klik S&K 1
        time.sleep(1)
        driver.find_element_by_xpath("//section[@id='sovia-payment']/form/div/div[2]/div[2]/div[3]/div/label").click() #Klik S&K 2
        time.sleep(1)
        driver.find_element_by_xpath("//section[@id='sovia-payment']/form/div/div[2]/div[2]/div[4]/div/label").click() #Klik S&K 3
        driver.find_element_by_id("next-step").click() #SUBMIT
        time.sleep(1)

        # Halaman Faspay
        driver.find_element_by_name("CARDNAME").click()
        driver.find_element_by_name("CARDNAME").send_keys("FASPAY")
        driver.find_element_by_name("CARDTYPE").click()
        driver.find_element_by_id("CARDNOSHOWFORMAT").click()
        driver.find_element_by_id("CARDNOSHOWFORMAT").send_keys("4111-1111-1111-1111")
        driver.find_element_by_name("CARDCVC").click()
        driver.find_element_by_name("CARDCVC").send_keys("101")
        driver.find_element_by_id("month").click()
        Select(driver.find_element_by_id("month")).select_by_visible_text("May")
        driver.find_element_by_id("month").click()
        driver.find_element_by_id("year").click()
        Select(driver.find_element_by_id("year")).select_by_visible_text("2021")
        driver.find_element_by_id("year").click()
        driver.find_element_by_name("submit").click()
        time.sleep(2)
        driver.find_element_by_link_text("LIHAT AKUN KAMU").click()
        time.sleep(6)
        driver.close()
        
        time.sleep(5)
    
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
