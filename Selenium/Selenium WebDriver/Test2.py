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
assert driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/section/div/div/div[1]/div/button")

driver.close()

