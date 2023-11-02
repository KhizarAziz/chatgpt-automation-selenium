# import pandas as pd
# import selenium
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import undetected_chromedriver as uc
from fake_useragent import UserAgent
import random

import constants


# creating options for the browser to
op = uc.ChromeOptions()
ua = UserAgent()
op.add_argument(f"--user-agent={ua.random}")# adding a random agent so that we dont get blocked.
op.add_argument('--no-first-run --no-service-autorun --password-store=basic')
op.add_argument("--user-data-dir=./website-data-cookies-etc")
op.add_argument("--headless")
# Further arguments are listed here: https://peter.sh/experiments/chromium-command-line-switches/

driver = uc.Chrome(version_main=118, options=op)

MAIL = constants.MAIL
PASSWORD = constants.PASS

driver.get('https://chat.openai.com/auth/login')

sleep(3)
i = 1
print('doing ste:',i)

inputElements = driver.find_elements(By.TAG_NAME, "button")
inputElements[0].click()

sleep(3)
print('doing ste:',i)

mail = driver.find_elements(By.TAG_NAME,"input")[1]
mail.send_keys(MAIL)

btn=driver.find_elements(By.TAG_NAME,"button")[0]
btn.click()

password= driver.find_elements(By.TAG_NAME,"input")[2]
password.send_keys(PASSWORD)

sleep(3)
print('doing ste:',i)

wait = WebDriverWait(driver, 10)
btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "_button-login-password")))
btn.click()
sleep(10)
print('doing ste:',i)

inputElements = driver.find_elements(By.TAG_NAME, "textarea")

prompt =  "what is 2+2?"
inputElements[0].send_keys(prompt)
sleep(2)
print('doing ste:',i)
inputElements[0].send_keys(Keys.ENTER)
sleep(10)
print('doing ste:',i)
inputElements = driver.find_elements(By.TAG_NAME, "p")
sleep(5)
print('doing ste:',i)
results = []
for element in inputElements:
    results.append(element.text)
    print(results)
sleep(10)
print('doing ste:',i)

# driver.quit()