from time import sleep
import undetected_chromedriver as uc
from fake_useragent import UserAgent


# creating options for the browser to
op = uc.ChromeOptions()

ua = UserAgent()
op.add_argument(f"--user-agent={ua.random}")# adding a random agent so that we dont get blocked.
op.add_argument('--no-first-run --no-service-autorun --password-store=basic')

driver = uc.Chrome(version_main=118, options=op)

driver.get('https://chat.openai.com/auth/login')

driver_ua = driver.execute_script("return navigator.userAgent")
print("User agent:",driver_ua) # Let print the random agent.
# Close the driver
driver.quit()
