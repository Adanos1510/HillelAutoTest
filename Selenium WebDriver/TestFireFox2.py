from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = Options()

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

SignInButton = driver.find_element(By.XPATH, "//button [@class='btn btn-outline-white header_signin']")
SignInButton.click()
Email = driver.find_element(By.XPATH, "(//input)[1]")
Email.send_keys("Pupsiki2group@gmail.com")
Password = driver.find_element(By.XPATH, "(//input)[2]")
Password.send_keys("Grupadva123")
remember = driver.find_element(By.NAME, "remember")
remember.click()
LoginButton = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-signin-modal/div[3]/button[2]")
LoginButton.send_keys(Keys.RETURN)

assert driver.find_element(By.XPATH, "//button [@class='btn btn-primary']")

driver.close()