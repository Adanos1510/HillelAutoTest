from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("start-maximized"); # open Browser in maximized mode
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service('C:\\Windows\\chromedriver.exe'), options=options)
driver.get("https://qauto2.forstudy.space/")

user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

time.sleep(2)
assert "Hillel Qauto" in driver.title


driver.close()