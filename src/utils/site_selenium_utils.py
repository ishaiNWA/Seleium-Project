

from selenium import webdriver # webdriver module providing classes to interact with various web browsers.
from selenium.webdriver.chrome.service import Service # imports the Service class for Chrome WebDriver
from webdriver_manager.chrome import ChromeDriverManager # imports the ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .site_page_elements import PageElements
from .site_test_data import TestData
from selenium.webdriver.chrome.options import Options
import time

###############################################################################
def setup_driver():
    chrome_options = Options()
    
    # Enable logging for all types of messages for the browser
    chrome_options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    
    # Add additional Chrome options for debugging
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--disable-popup-blocking')
    
    # Create a Service object using ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    
    # Create an instance of the Chrome WebDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver

###############################################################################
def check_page_errors(driver ):
    logs = driver.get_log("browser")
    errors = []
    for log in logs:
        if log["level"] in ['SEVERE', 'ERROR'] :
            errors.append(log)
            print(f"log is : {log}")
            
    return errors

###############################################################################
def clear_browser_error_logs(driver):
    print(f"clearance of : ${driver.current_url}")
    driver.get_log('browser')  # This actually clears the logs as it retrieves them

###############################################################################
def is_422_status_code(driver):
    logs = driver.get_log("browser")
    for log in logs:
        if 'status of 422' in log['message']:
            return True
    
    return False
###############################################################################

def extract_language_urls(driver):
    
    lang_menu_list = wait_for_element_to_be_located(driver ,PageElements.LANGUAGE_MENU)
    # Find all language option elements
    lang_raw_items = lang_menu_list.find_elements(By.TAG_NAME, "li") 
    
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
def fill_reg_form(driver):
        
    time.sleep(5)
    first_name_form_element = wait_for_element_to_be_located(driver , PageElements.FIRST_NAME)
    last_name_form_element = wait_for_element_to_be_located(driver , PageElements.LAST_NAME)
    email_form_element = wait_for_element_to_be_located(driver , PageElements.EMAIL)

    time.sleep(5)
    # Clear and fill the form fields
    for element , data_key in [
        (first_name_form_element , "first_name"),
        (last_name_form_element, "last_name"),
        (email_form_element, "email")
    ]:    
        element.clear()
        element.send_keys(TestData.forms[data_key])
        
    wait_for_element_and_click(driver , PageElements.SUBMMIT_CREDENTIAL_BUTTON)
          
    # Wait for and click the country selection container
    wait_for_element_and_click(driver , PageElements.COUNTRY_CONTAINER)

    # Wait for and click the Great Britain option
    wait_for_element_and_click(driver, PageElements.GB_OPTION)    
    
    phone_number_form_element = wait_for_element_to_be_located(driver , PageElements.PHONE_NUMBER)
    phone_number_form_element.clear()
    phone_number_form_element.send_keys(TestData.forms["phone_number"])
          
###############################################################################
def register(driver, register_button):
    
    old_url = driver.current_url
    register_button.click()
    WebDriverWait(driver, 15).until(EC.url_changes(old_url))

###############################################################################
def get_register_button(driver , timeout = 15):
    return WebDriverWait(driver,timeout).until(
        EC.element_to_be_clickable( PageElements.REGISTER_BUTTON))
    
###############################################################################
def wait_for_element_and_click(driver , element, timeout = 15):
    clickable_element = WebDriverWait(driver, timeout ).until(
        EC.element_to_be_clickable(element)
    )
    clickable_element.click()

###############################################################################
def wait_for_element_to_be_located(driver , element, timeout = 15):
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
   