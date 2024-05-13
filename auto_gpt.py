import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from time import sleep
from random import uniform
from constants import MAIN_URL, LOGIN_METHOD, MAIL, PASS, CHROME_OPTIONS_ARGS, DEFAULT_WAIT_BEFORE_ACTION_TIME
import yaml

class AutoGPT:
    """
    A class to automate browser actions using Selenium with undetected Chromedriver.
    
    Methods
    -------
    setup_driver():
        Sets up the Chrome driver with specified options.
        
    load_yaml(file_path):
        Loads YAML configuration from the specified file path.
        
    wait_with_random_delay(delay_range):
        Pauses execution for a random amount of time within the specified range.
        
    perform_action(config):
        Executes a browser action based on the provided configuration.
        
    login():
        Logs into a website using predefined credentials and methods.
        
    enter_prompt(prompt_text):
        Enters a prompt into a text area and retrieves the response.
    """
    def __init__(self):
        self.driver = self.setup_driver()
        self.selectors_config = self.load_yaml('element_selectors.yaml')
        # print("Driver setup done!")
        self.driver.get(MAIN_URL)
        self.login()
        # print("Login done!")

    def setup_driver(self):
        """Configures and returns a Chrome WebDriver with random user-agent and additional options from constants."""
        chrome_options = Options()
        ua = UserAgent()
        chrome_options.add_argument(f"--user-agent={ua.random}")
        for arg in CHROME_OPTIONS_ARGS:
            chrome_options.add_argument(arg)
        return uc.Chrome(options=chrome_options)

    def load_yaml(self, file_path):
        """Loads YAML configuration from the specified file."""
        with open(file_path, 'r') as config_file:
            return yaml.safe_load(config_file)

    def wait_with_random_delay(self, delay_range=(0.5, 2.0)):
        """Pauses the program for a random time within the given range to mimic human interaction."""
        sleep(uniform(*delay_range))

    def perform_action(self, config):
        """Executes specified actions like clicking, inputting text, and reading text based on the configuration."""
        wait = WebDriverWait(self.driver, 15)
        selector = config['selector']
        action_type = config['action']
        wait_times = config.get('wait_before_action', DEFAULT_WAIT_BEFORE_ACTION_TIME)
        self.wait_with_random_delay(wait_times)

        try:
            if action_type == 'clickable':
                element = wait.until(EC.element_to_be_clickable((By.XPATH, selector) if selector.startswith("//") else (By.CSS_SELECTOR, selector)))
                element.click()
            elif action_type == 'input_field':
                element = wait.until(EC.visibility_of_element_located((By.XPATH, selector) if selector.startswith("//") else (By.CSS_SELECTOR, selector)))
                element.send_keys(config['input_value'])
            elif action_type == 'readable':
                elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, selector) if selector.startswith("//") else (By.CSS_SELECTOR, selector)))
                return [element.text for element in elements]
            else:
                raise ValueError(f"Action type '{action_type}' not supported.")
        except Exception as e:
            raise ValueError(f"Action Failed on selector {selector} with error {str(e)}")

    def login(self):
        """Logs into the website using predefined YAML configurations for user interactions."""
        config_page = self.selectors_config['login_page']
        self.perform_action(config_page['login_button'])
        login_method = LOGIN_METHOD
        method_elements = config_page[login_method]['elements']
        method_elements['email_input']['input_value'] = MAIL
        self.perform_action(method_elements['email_input'])
        self.perform_action(method_elements['next_button'])
        method_elements['password_input']['input_value'] = PASS
        self.perform_action(method_elements['password_input'])
        self.perform_action(method_elements['final_login_button'])

    def enter_prompt(self, prompt_text) -> list :
        """Submits a text prompt on a page and returns the response as text."""
        config_page = self.selectors_config['prompt_page']
        config_page['prompt_textarea']['input_value'] = prompt_text
        self.perform_action(config_page['prompt_textarea'])
        self.perform_action(config_page['submit_prompt_button'])
        prompt_response_elements = self.perform_action(config_page['prompt_response_elements'])
        return prompt_response_elements
    
    def quit(self):
        """Quit Driver upon action done!"""
        self.wait_with_random_delay()
        self.driver.quit()
