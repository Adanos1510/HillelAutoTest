from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("disable-infobars");
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service('C:\\Windows\\chromedriver.exe'), options=options)
driver.get("https://qauto2.forstudy.space/")

user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

time.sleep(2)
assert "Hillel auto developed in Hillel IT school for educational purposes of QA courses." in driver.page_source

driver.close()