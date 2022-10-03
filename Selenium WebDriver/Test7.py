from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("disable-infobars");
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service('C:\\Windows\\chromedriver.exe'), options=options)
driver.get("https://qauto2.forstudy.space/")

user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()

email = driver.find_element(By.NAME, "email")
email.send_keys("Pupsiki2group@gmail.com")

password = driver.find_element(By.NAME, "password")
password.send_keys("Grupadva123")

remember = driver.find_element(By.NAME, "remember")
remember.click()

login = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[2]")

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Login')]"))).click()
time.sleep(2)

assert "h1" in driver.page_source
driver.close()