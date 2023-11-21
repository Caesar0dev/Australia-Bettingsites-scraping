import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import pyautogui
import subprocess


options = uc.ChromeOptions()
browser = uc.Chrome(options=options)

# Make sure to include the protocol (http or https) in the URL
url = 'https://www.neds.com.au'
browser.get(url)

browser.maximize_window()