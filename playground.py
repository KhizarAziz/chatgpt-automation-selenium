import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from time import sleep
from random import uniform
import constants
import yaml


# Assuming YAML file is named 'element_selectors.yaml' and is in the same directory as your script
with open('element_selectors.yaml', 'r') as config_file:
    selectors_config = yaml.safe_load(config_file)

# Function to introduce a random short delay before performing an action
def wait_with_random_delay(delay_range=(0.5, 2.0)):
    sleep(uniform(*delay_range))

# creating options for the browser to use
chrome_options = Options()
ua = UserAgent()
chrome_options.add_argument(f"--user-agent={ua.random}")  # adding a random agent so that we don't get blocked.
chrome_options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
chrome_options.add_argument("--user-data-dir=./website-data-cookies-etc")
# chrome_options.add_argument("--headless")

driver = uc.Chrome(version_main=119,options=chrome_options) # creating a chrome driver object

print('Chrome Driver Created')

driver.get(constants.MAIN_URL)

# Function to perform action based on YAML config
def perform_action(driver, config):
    wait = WebDriverWait(driver, 15)
    selector = config['selector']
    action_type = config['action']
    wait_times = config.get('wait_before_action', [0, 0])
    
    # Random wait before action
    sleep(uniform(*wait_times))

    try:
        if action_type == 'clickable':
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
            button.click()
        elif action_type == 'input_field':
            print("input value was :",config['input_value'])
            text_to_input = config['input_value']
            input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            input_field.send_keys(text_to_input)
        
        elif action_type == 'readable':
            return wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))
        else:
            raise ValueError(f"Action type '{action_type}' not supported.")
    except Exception as e:
        error_message = str(e)  # Replace this with the actual error message
        raise ValueError(f"Action Failed on selector {selector}  with error {error_message}")
        
        # raise ValueError(f"Action Failed on selector {(config.keys())[0]}: with error ")



'''
###########################################################################
                            ON LOGIN PAGE
###########################################################################
'''

config_page = selectors_config['login_page']

# login
print('login')
perform_action(driver, config_page['login_button'])

print('login with google')
perform_action(driver, config_page['login_with_google'])

# enter email
print('enter email')
config_page['email_input']['input_value'] = constants.MAIL
perform_action(driver, config_page['email_input'])

# click continue
print('click continue')
perform_action(driver, config_page['next_button'])

# enter pass
print('enter pass')
config_page['password_input']['input_value'] = constants.PASS
perform_action(driver, config_page['password_input'])

# finally login
print('click login')
perform_action(driver, config_page['final_login_button'])

'''
###########################################################################
                            ON PROMPT PAGE
###########################################################################
'''
config_page = selectors_config['prompt_page']

# enter text prompt
print('enter prompt')
config_page['prompt_textarea']['input_value'] = "what is the value of 233 + 67?"
perform_action(driver, config_page['prompt_textarea'])

# sent prompt
print('send prompt')
perform_action(driver, config_page['submit_prompt_button'])

# fetch response
print('recv response of prompt')
prompt_response_elements = perform_action(driver, config_page['prompt_response_elements'])
results = [element.text for element in prompt_response_elements]
print(results)

sleep (20)
# Continue replacing the rest of the interactions similarly...
driver.quit()
