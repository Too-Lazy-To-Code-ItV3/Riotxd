import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from msedge.selenium_tools import Edge,EdgeOptions
from selenium.webdriver.opera.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

#OperaGx error keybinds w zahi 
#opera_options = Options()
#opera_options.binary_location = 'C:\\Users\\Adam\\AppData\\Local\\Programs\\Opera GX\\launcher.exe'
#driver = webdriver.Opera(options=opera_options, executable_path="C:\\SHIT\\opera\\operadriver_win64\\operadriver.exe")

os.environ['PATH'] += ';C:\\Users\\Adam\\.cache\\selenium\\msedgedriver\\win64\\112.0.1722.58'

options = EdgeOptions()
options.use_chromium = True
driver = Edge(options=options)



driver.get('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjG4eTx17z-AhXK7rsIHdlJA3EQFnoECAYQAQ&url=https%3A%2F%2Faccount.riotgames.com%2F&usg=AOvVaw0EHp9u_JUpUOqYeppGN9Xr')

username_field = driver.find_element_by_name('username')
password_field = driver.find_element_by_name('password')

username_field.send_keys('username')
password_field.send_keys('password')

wait = WebDriverWait(driver, 10)
login_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/button')))
login_button.click()

time.sleep(5) # or use WebDriverWait to wait for a specific element to appear


