

from selenium import webdriver # webdriver module providing classes to interact with various web browsers.
from selenium.webdriver.chrome.service import Service # imports the Service class for Chrome WebDriver
from webdriver_manager.chrome import ChromeDriverManager # imports the ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from .site_page_elements import PageElements
from .site_test_data import TestData
import subprocess
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

###############################################################################
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

# Conditional imports
import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from immediatfolex_page_elements import PageElements
    from immediatfolex_test_data import TestData
except ImportError:
    from utils.immediatfolex_page_elements import PageElements
    from utils.immediatfolex_test_data import TestData

import subprocess

"""

##############################################################################

"""

def setup_driver():
    print("VPN connection - setup_driver")
    # Connect to NordVPN UK server
    server = "UK"
    try:
        print(f"Attempting to connect to NordVPN server: {server}")
        result = subprocess.run(["nordvpn", "connect", server], capture_output=True, text=True, check=True)
        print("NordVPN connection attempt completed")
        print("Stdout:", result.stdout)
        print("Stderr:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to NordVPN server {server}. Error:")
        print("Stdout:", e.stdout)
        print("Stderr:", e.stderr)
        print("Return code:", e.returncode)
        return None
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
     # enables logging -for all types of messages- for the  browser
    chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    
    # Create a Service object using ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    
    # Create and return the Chrome WebDriver instance
    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        return driver
    except Exception as e:
        print(f"Failed to create WebDriver: {e}")
        return None
"""
##############################################################################


def setup_driver():
    
    chrome_options = Options()
    
    # enables logging -for all types of messages- for the  browser
    chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    
    # creates a Service object, which is used to define how the WebDriver 
    # should start and stop the browser driver process.
       # Create a Service object using ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    
     # creates an instance of the Chrome WebDriver. allowing interaction with a browser
    driver = webdriver.Chrome(service=service,options=chrome_options)
    return driver

###############################################################################

def check_page_errors(driver , ignore_422 = False):
    logs = driver.get_log("browser")
    errors = []
    for log in logs:
        if log["level"] in ['SEVERE', 'WARNING' , 'ERROR'] :
            if ignore_422 and "status of 422" in log['message'] and "split-registration" in log['message']:                continue
            else:
                errors.append(log)
                print(f"log is : {log}")
                
    return errors

###############################################################################

def extract_language_urls(driver):
    
        # Wait for the language menu to be present
    lang_menu_list = wait_for_element_to_be_located(driver ,PageElements.LANGUAGE_MENU)
    # Find all language option elements
    lang_raw_items = lang_menu_list.find_elements(By.TAG_NAME, "li") 
    # create map to store language codes and their URLs
    lang_map ={'en': "https://immediatfolex.ai/"} # Add default language (English) to the map
    
    for item in lang_raw_items:      
        #parse the language code
        lang_code = item.get_attribute("id").split("-")[-1]
        lang_link_element = item.find_element(By.TAG_NAME, "a")
        #extract language's page url
        lang_url = lang_link_element.get_attribute("href")
        lang_map[lang_code] = lang_url
        

    return lang_map

###############################################################################

def fill_lang_forms(driver):
    
   
        first_name_form_element = wait_for_element_to_be_located(driver , PageElements.FIRST_NAME)
        last_name_form_element = wait_for_element_to_be_located(driver , PageElements.LAST_NAME)
        email_form_element = wait_for_element_to_be_located(driver , PageElements.EMAIL)

        # Clear and fill the form fields
        for element , data_key in [
            (first_name_form_element , "first_name"),
            (last_name_form_element, "last_name"),
            (email_form_element, "email")
        ]:    
            element.clear()
            element.send_keys(TestData.forms[data_key])
            
        
            submmit_creds_button_form_element = wait_for_element_to_be_clickable(driver , PageElements.SUBMMIT_CREDENTIAL_BUTTON)
            submmit_creds_button_form_element.click()
               
        # Wait for and click the country selection container
        country_container = wait_for_element_to_be_clickable(driver , PageElements.COUNTRY_CONTAINER)
        country_container.click()

        # Wait for and click the Great Britain option
        gb_option = wait_for_element_to_be_clickable(driver, PageElements.GB_OPTION)    
        gb_option.click()
        
        phone_number_form_element = wait_for_element_to_be_clickable(driver , PageElements.PHONE_NUMBER)
        phone_number_form_element.clear()
        phone_number_form_element.send_keys(TestData.forms["phone_number"])
          
        
###############################################################################

def redirect_page(driver, redirect_button):
    
    old_url = driver.current_url
    redirect_button.click()
    WebDriverWait(driver, 10).until(EC.url_changes(old_url))

###############################################################################
def get_redirect_button(driver , timeout = 10):
    return wait_for_element_to_be_clickable(driver, PageElements.REDIRECT_BUTTON)
    
###############################################################################

def wait_for_element_to_be_clickable(driver , element, timeout = 10):
    return WebDriverWait(driver, timeout ).until(
        EC.element_to_be_clickable(element)
    )

###############################################################################
    
def wait_for_element_to_be_located(driver , element, timeout = 10):
        return WebDriverWait(driver, timeout ).until(
        EC.presence_of_element_located(element)
    )
    
###############################################################################
       
def main():
    driver = setup_driver()
    url = "https://jsbin.com/badscript"
    driver.get(url)
    errors = check_page_errors(driver)
    if errors:
        print("Errors found:")
        for error in errors:
            print(error)
    else:
        print("No errors found.")
    driver.quit()

if __name__ == "__main__":
    main()
   