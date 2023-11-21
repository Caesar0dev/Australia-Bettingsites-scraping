from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import pandas as pd
import time
import re
import csv
from datetime import datetime
from datetime import date
from seleniumbase import Driver

driver = Driver(uc=True)
driver.maximize_window()
url = 'https://www.topsport.com.au/'
driver.get(url)


# # Click the "Log In" button
# login_button = driver.find_element(By.XPATH, "//button[@data-testid='header-login']")
# login_button.click()

# Wait for 3 seconds
time.sleep(3)

# Find and type in the username
username_input = driver.find_element(By.XPATH, "//input[@id='login_username']")
username_input.send_keys("122347")

# Wait for 3 seconds
time.sleep(3)

# Find and type in the password
password_input = driver.find_element(By.XPATH, "//input[@id='login_password']")
password_input.send_keys("Angel0924")

# Wait for 3 seconds
time.sleep(3)

# Click the "Log In" button again to submit the form
login_submit_button = driver.find_element(By.XPATH, '//*[@id="loginSubmit"]')
login_submit_button.click()

# Wait for the popup to appear (adjust sleep time as needed)
time.sleep(10)  # Increased sleep time before Save button
#

while True:
    pass
# # driver.close()
