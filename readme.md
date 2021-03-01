<p align="center">
  <img src="https://i.ibb.co/djnLFxG/ux-design.png" height="80" /><br/>
  <span><b>Superyou</b>: :robot: <span>Automation Testing</span><br/>
  <b>V2</b>
</p>
  
<br/>

## Python Selenium
https://selenium-python.readthedocs.io/api.html

Steps to implement and execute Automation Test:

1. Install Python:
https://www.python.org/downloads/

2. Install Selenium by entering the following commands into the Terminal:
- Windows: `pip install Selenium`
- Mac: `pip3 install Selenium`

#### If you use Google Chrome:

3. Navigate to <a href="https://sites.google.com/a/chromium.org/chromedriver/home">Chrome Driver</a> and download the WebDriver that matches the version of your Google Chrome Browser
4. Extract the file from the folder and put it in your C: drive so your PATH would be `C:\chromedriver.exe`
5. Initialize the path in the file by writing this code:
`PATH = "C:\chromedriver.exe`
6. Make sure that the webdriver code is `self.driver = webdriver.Chrome(PATH)` instead of `self.driver = webdriver.Edge(PATH)`

#### If you use Microsoft Edge:

3. Ensure that you have Microsoft Edge (Chromium) installed by navigating to `edge://settings/help` and verify that the version number is version 75 or later
4. Navigate to <a href="https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/">Microsoft Edge Driver</a> and download the WebDriver that matches the version of your Microsoft Edge
5. Extract the file from the folder and put it in your C: drive so your PATH would be `C:\msedgedriver.exe`
6. Open the repository on your text editor and open your terminal. Enter the following command:
`pip install msedge-selenium-tools selenium==3.141`
7. Initialize the path in the file by writing this code:
`PATH = "C:\msedgedriver.exe`
8. Make sure that the webdriver code is `self.driver = webdriver.Edge(PATH)` instead of `self.driver = webdriver.Chrome(PATH)`


A few ways to run automation test:
- Visual Code: Press the Play Button (Top Right Corner)
- Terminal (Windows): Press `python testcase_login` then click Enter
- Terminal (Mac): Press `python3 testcase_login` then click Enter

###For references:
Microsoft Edge Installation: https://docs.microsoft.com/en-us/microsoft-edge/webdriver-chromium/?tabs=python
