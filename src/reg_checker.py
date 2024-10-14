from .utils.site_selenium_utils import setup_driver, extract_language_urls, fill_lang_forms, get_redirect_button, redirect_page, check_page_errors
import time
from requests.exceptions import ConnectionError, Timeout
from .exceptions import pageCheckError
import logging
import logging.config
import yaml
from pathlib import Path
from selenium.common.exceptions import TimeoutException,NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException


###############################################################################

# Load the logging configuration
config_path = Path(__file__).parent.parent / 'config' / 'log_config.yaml'
with open(config_path, 'r') as log_config_file:
    config = yaml.safe_load(log_config_file)
    logging.config.dictConfig(config['logging'])  # Configure the logging system

 # create logger objects 
internal_error_logger = logging.getLogger('internal_errors')
redirection_error_logger = logging.getLogger('redirection_error')
page_errors_logger = logging.getLogger('page_errors')

###############################################################################
"""
def check_redirections_in_page(base_page_url):
    driver = setup_driver()
    if driver is None:
        internal_error_logger.error("Failed to set up WebDriver. NordVPN connection may have failed.")
        return  # Exit the function if driver setup failed

    driver.get(base_page_url)
    page_errors = check_page_errors(driver)
    if page_errors:
        for error in page_errors:
            page_errors_logger.error(f"Errors in {base_page_url}: {error} ")
    
    lang_map = extract_language_urls(driver)
    print(f"map length: {len(lang_map)}")
     
    for lang_code , lang_page_url in lang_map.items():
        print(f"{lang_code}-{lang_page_url}")
        driver.get(lang_page_url)
        page_errors = check_page_errors(driver)
        if page_errors:
            for error in page_errors:
                page_errors_logger.error(f"Errors in {lang_page_url}: {error} ")
        
        #invoke fill_reg_forms_with_test_data
        fill_lang_forms(driver)
        try:
            validate_registration_redirection(driver)
    
        except RedirectionError as e:
            redirection_error_logger.error(f"failed to redirect from {e.current_url}") 
            send_telegram_alarm(f"failed to redirect from {e.current_url}")
           
        except(ConnectionError, Timeout, NoSuchElementException, 
               ElementClickInterceptedException) as e:
            internal_error_logger.error(f"Internal error: {e}")
            
        except StaleElementReferenceException as e:
            internal_error_logger.error(f"Stale Exception: {e}")
            
        except Exception as e:
            # This will show you the full traceback for any unhandled exception
            print(f"An error occurred while checking {lang_code}:")
            traceback.print_exc()
    
    send_telegram_alarm(f"system has finished redirectio cheking for {base_page_url}")        
    driver.quit()
"""   
###############################################################################

#wraper for 422
# and redirection button
#boolean

def is_valid_reg(driver):
     
    time.sleep(3)
    try:
        page_errors = check_page_errors(driver , True)
        if page_errors:
            raise pageCheckError(driver.current_url, page_errors)
        
        redirect_button = get_redirect_button(driver)
        redirect_page(driver, redirect_button) 
        time.sleep(5)  
        return True
        
    except TimeoutException as e:
        #TimeoutException indicated invalid registraion
        return False
###############################################################################

    """
 
def check_links_in_page(base_url):
    driver = setup_driver()
    driver.get(base_url)  # Navigate to the page  
    links_in_page = driver.find_elements(By.TAG_NAME, 'a')
    broken_link_logger.info(f"Checking links on page: {base_url}")
    #TODO list of languages
    
    #TODO iterate languages each languache is sent to valdate_registration_for_language

    for link in links_in_page:
        link_url = link.get_attribute('href')
        try:
            validate_link(base_url, link_url)
        except BrokenLinkError as e:
            broken_link_logger.error(f"Broken link found: {e}")
            asyncio.run(send_telegram_alarm(f"ERROR ALARM for url: {e.url}. status: {e.status_code}"))
        except (ConnectionError, Timeout) as e:
            internal_error_logger.error(f"Internal error: {e}")

    driver.quit()
    broken_link_logger.info("Finished checking links")

   """
###############################################################################

"""""
def validate_link(base_url, link_url , max_retries = 5):

    full_link_url = urljoin(base_url, link_url)
    
    for attempt in range(max_retries):
        try:
            get_response = requests.get(full_link_url, allow_redirects=True, timeout=5)

            if get_response.status_code >= 400:
                raise BrokenLinkError(
                        url=full_link_url,
                        status_code=get_response.status_code,
                        error_content=get_response.text[:200]
                )
            else:
                broken_link_logger.debug(f"Valid link: {full_link_url} (Status: {get_response.status_code})")
                return  # Success, exit the function

        except (ConnectionError, Timeout) as e:
            if attempt + 1 == max_retries:
                raise e
            else:
                time.sleep(1)  # Wait before the next retry
       
    """
###############################################################################    
        