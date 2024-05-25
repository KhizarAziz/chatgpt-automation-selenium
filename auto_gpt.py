import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from time import sleep
from random import uniform
from .configs import CHROME_OPTIONS_ARGS, DEFAULT_WAIT_BEFORE_ACTION_TIME, ELEMENT_SELECTORS_YAML_PATH,GPT_EMAIL,GPT_PASSWORD
import yaml
from collections import defaultdict


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
    def __init__(self, main_url,login_needed = False, login_type=''):
        self.selectors_config = self.load_yaml(ELEMENT_SELECTORS_YAML_PATH)
        print("Setting up Driver ...! (If taking too long, chromedriver updating on slow internet OR chrome app is currepted (clear default profile)!)")
        self.driver = self.setup_driver()
        print("Getting Website...!")
        self.driver.get(main_url)
        print("Driver setup done, now logging in...!")
        if login_needed:
            self.login(login_type)
        print("Login done, now prompting...!")

    def setup_driver(self):
        """Configures and returns a Chrome WebDriver with random user-agent and additional options from constants."""
        chrome_options = Options()
        ua = UserAgent()
        chrome_options.add_argument(f"--user-agent={ua.random}")
        for arg in CHROME_OPTIONS_ARGS:
            chrome_options.add_argument(arg)
        try:
            # Attempt to initialize the Chrome driver
            driver = uc.Chrome(options=chrome_options)
            print("driver created..!")
        except Exception as e:
            # Print the error message
            print(f"Error occurred: {e}")
            print("------------------------------------------------------------------------------------------------------------")
            print("# If chrome driver version issue, please update lib : pip install undetected-chromedriver --upgrade")
            print("#      1.update Chrom Browser: Chrome -> Help -> About Google Chrome -> Update")
            print("#      2. pip install undetected-chromedriver --upgrade")
            print("------------------------------------------------------------------------------------------------------------")
            exit()
        return driver

    def load_yaml(self, file_path):
        """Loads YAML configuration from the specified file."""
        with open(file_path, 'r') as config_file:
            return yaml.safe_load(config_file)

    def wait_with_random_delay(self, delay_range=(0.5, 2.0)):
        """Pauses the program for a random time within the given range to mimic human interaction."""
        sleep(uniform(*delay_range))

    # Function to perform action based on YAML config
    def perform_action(self, config):
        wait = WebDriverWait(self.driver, 15)
        selector = config['selector']
        action_type = config['action']
        wait_time_s = config.get('wait_before_action', DEFAULT_WAIT_BEFORE_ACTION_TIME)
        self.wait_with_random_delay(wait_time_s) # Random wait before action

        print(f"Doing ActionType: {action_type}  -  Selector {selector} , Waiting {wait_time_s} seconds")
        try:
            if action_type == 'clickable':
                if selector.startswith("//"):  # Indicates an XPath selector
                    button = wait.until(EC.element_to_be_clickable((By.XPATH, selector)))
                else:  # Defaults to CSS Selector
                    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                button.click()
            elif action_type == 'input_field':
                text_to_input = config['input_value']
                if selector.startswith("//"):  # Indicates an XPath selector
                    input_field = wait.until(EC.visibility_of_element_located((By.XPATH, selector)))
                else:  # Defaults to CSS Selector
                    input_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
                input_field.send_keys(text_to_input)
            elif action_type == 'readable':        
                if selector.startswith("//"):  # Indicates an XPath selector
                    return wait.until(EC.visibility_of_all_elements_located((By.XPATH, selector)))
                else:  # Defaults to CSS Selector
                    return wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, selector)))
            else:
                raise ValueError(f"Action type '{action_type}' not supported.")
        except Exception as e:
            error_message = str(e)  # Replace this with the actual error message
            print(f"Action Failed on selector {selector}  with error {error_message}")
            # raise ValueError()
            exit()

    def login(self, login_type) -> None:
        """Logs into the website using predefined YAML configurations for user interactions."""
        config_page = self.selectors_config['login_page']
        self.perform_action(config_page['login_button'])
        method_elements = config_page[login_type]['elements'] # there
        method_elements['email_input']['input_value'] = GPT_EMAIL
        self.perform_action(method_elements['email_input'])
        self.perform_action(method_elements['next_button'])
        method_elements['password_input']['input_value'] = GPT_PASSWORD
        self.perform_action(method_elements['password_input'])
        self.perform_action(method_elements['final_login_button'])

    # def enable_temporary_new_chat(self) -> None:
    #     """This method opens a new chat and enable temporary chat mode."""
    #     print("Temping chat in 10 sec")
    #     home_page = self.selectors_config['home_page']
    #     self.perform_action(home_page['Chat_GPT_dropdown_button']) # clicking new chat button
    #     print("clicked dropdown")
    #     self.perform_action(home_page['temporary_chat_switch']) # clicking new chat button        
    #     print("clicked switch, now sleeping")


    def refresh_page_to_start_new_chat(self):
        # Refresh the page
        print("refersing page")
        self.driver.refresh()

    
    def enter_prompt(self, prompt_text,start_new_chat=False) -> defaultdict:
        """Submits a text prompt on a page and returns the response as text."""
        if start_new_chat:
            self.refresh_page_to_start_new_chat()
        config_page = self.selectors_config['prompt_page']
        config_page['prompt_input_text_field']['input_value'] = prompt_text
        self.perform_action(config_page['prompt_input_text_field'])
        # self.perform_action(config_page['submit_prompt_button']) # prompt submit button is no more needed!
        # results = [element.text for element in whole_conversation] # extracting values from each of chat bubble
        whole_conversation = self.perform_action(config_page['conversation_listview'])
        last_message_element = whole_conversation[-1]
        
        
        message_dict = defaultdict()
        message_dict['text'] = last_message_element.text # last message in the gpt chat
        
        
        image_elements = last_message_element.find_elements(By.TAG_NAME, 'img') # Locate all images in last_message_element
        if len(image_elements) > 0:
            message_dict['img_url'] = image_elements[-1].get_attribute('src') # getting the last image's source
            print("Images found: ",message_dict['img_url'])
        return message_dict
    
    def quit(self):
        """Quit Driver upon action done!"""
        self.wait_with_random_delay()
        self.driver.quit()
