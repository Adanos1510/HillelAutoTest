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
elem = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/app-header/header/div/div/div[2]/button[2]")
elem.click()
time.sleep(2)

email = driver.find_element(By.NAME, "email")
email.send_keys("Pupsiki2group@gmail.com")

password = driver.find_element(By.NAME, "password")
password.send_keys("Grupadva123")

remember = driver.find_element(By.NAME, "remember")
remember.click()

login = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[2]")
login.click()

time.sleep(2)

assert "You don’t have any cars in your garage" in driver.page_source

driver.close()