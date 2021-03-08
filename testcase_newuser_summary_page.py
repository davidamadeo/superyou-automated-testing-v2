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

# Data Akun
Email = "smith0004@email.com" # Wajib Unik
Phone = "081234560004" # Wajib Unik

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
 
class TestCaseSingleProduct(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(PATH)
        # self.driver = webdriver.Chrome(PATH)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_case_NewUser_SingleProduct(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://staging.superyou.co.id/") #Link Website
        time.sleep(1) #In Second

        # Go to Super Strong product page
        driver.find_element_by_xpath("/html/body/div[3]/header/div[4]/div/div/div[2]/div[1]/div[1]/div/div[3]/a").click() #Super Strong Product Page Button
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/div/div[3]/div[1]/div/div/div/div[3]/a").click() #Pilih Plan Ini Button
        time.sleep(1)
        driver.find_element_by_xpath("//input[@type='tel']").send_keys(TglLahir) #Input Tanggal Lahir Tertanggung
        driver.find_element_by_xpath("(//input[@type='tel'])[2]").send_keys(BlnLahir) #Input Bulan
        driver.find_element_by_xpath("(//input[@type='tel'])[3]").send_keys(ThnLahir) #Input Tahun
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/section/div/div/div[2]/div[1]/div/div[3]/ul/li/div/a").click() #Klik Beli Plan
        time.sleep(1)

        # Klik Tombol Keranjang
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div/div/img").click() #Klik Tombol Keranjang
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[1]/div[5]/div/div[2]/div").click() #Klik Lanjut Beli

        #Pengisi Form Isi Data
        time.sleep(3)
        driver.find_element_by_name("name").click()
        driver.find_element_by_name("name").send_keys(Name) #Input Nama
        driver.find_element_by_xpath("//div[@id='form-user']/div[2]/div/div[3]/div/div[3]/div/div/div/label").click() #Select Gender: Male
        driver.find_element_by_name("citizen_id").click()
        driver.find_element_by_name("citizen_id").send_keys(KTP) #Input No. KTP (16 digits)
        driver.find_element_by_name("urban_district").click()
        driver.find_element_by_name("urban_district").send_keys(Kelurahan) #Input Kelurahan
        driver.find_element_by_name("city").click()
        driver.find_element_by_name("city").send_keys(Kota) #Input Kota
        driver.find_element_by_name("phone").click()
        driver.find_element_by_name("phone").send_keys(Phone) #Input No. Handphone
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").send_keys(Email) #Input Email
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
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[3]/div/div[15]/button").click() #Click Button SUBMIT
        time.sleep(1)

        # Halaman Rincian Tertanggung
        driver.find_element_by_xpath("//div[@id='su-base-select']/div[2]/div/div").click() #Click Status Tertanggung
        driver.find_element_by_xpath("//div[@id='su-base-select']/div[2]/ul/li").click() #Select Tertanggung (Diri Sendiri)
        driver.find_element_by_xpath("(//div[@id='su-base-select']/div/div)[4]").click() #Click Daftar Pekerjaan
        driver.find_element_by_xpath("//div[@id='su-base-select']/div/ul/li[16]").click() #Select Pekerjaan (Karyawan Swasta)
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[4]/div/div[7]/button").click() #Lanjut Button (Halaman Rincian Tertanggung)
        time.sleep(1)

        # Halaman Ahli Waris
        driver.find_element_by_xpath("(//input[@type='search'])[5]").click() #Click Daftar Ahli Waris
        driver.find_element_by_xpath("//div[@id='su-base-select']/div[2]/ul/li[4]").click() #Select Daftar Ahli Waris
        driver.find_element_by_xpath("(//input[@name='name'])[3]").click()
        driver.find_element_by_xpath("(//input[@name='name'])[3]").send_keys(NamaAhliWaris) #Input Ahli Waris
        driver.find_element_by_xpath("(//input[@type='tel'])[11]").click()
        driver.find_element_by_xpath("(//input[@type='tel'])[11]").send_keys(TglLahirAhliWaris) #Input Tanggal Lahir Ahli Waris
        driver.find_element_by_xpath("(//input[@type='tel'])[12]").send_keys(BlnLahirAhliWaris) #Input Bulan Ahli Waris
        driver.find_element_by_xpath("(//input[@type='tel'])[13]").send_keys(ThnLahirAhliWaris) #Input Tahun Ahli Waris
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div/div[3]/div/div[1]/div/img").click() #Click Calendar Button
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[5]/div/div[3]/div/div[1]/div/img").click() #Click Calendar Button
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='form-user']/div[2]/div/div[5]/div/div[5]/button").click() #Submit Button (Halaman Rincian Tertanggung)
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

        time.sleep(300)

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