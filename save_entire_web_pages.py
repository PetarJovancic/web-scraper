import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

### please adjust user input
url='xxxxxxxx'
reference_url='xxxxx'
user="xxxxxx"
password="xxxxxxxxx"
token="xxxxxx"

### open url in Chrome web browser
driver=webdriver.Chrome(executable_path='xxxxxxx')
driver.get(url)
driver.maximize_window()

### Login in
driver.implicitly_wait(20)
driver.find_element_by_id("username").clear()
driver.find_element_by_id("username").send_keys(user)
driver.find_element_by_id("password").clear()
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_id("login").click()
driver.find_element_by_id("xxxxx").send_keys(token)
driver.find_element_by_id("login").click()
time.sleep(2)

### Save web pages
while True:
    check_url = driver.current_url
    print(check_url)
    time.sleep(2)
    if check_url != reference_url:
        pyautogui.hotkey('ctrl', 's')
        time.sleep(2)
        pyautogui.hotkey('enter')
        time.sleep(1)
        driver.find_element_by_xpath('xxxxxxxx').click()
        time.sleep(2)
    else:
        driver.quit()
