from .utils.site_selenium_utils import  get_register_button, register, check_page_errors, is_422_status_code, clear_browser_error_logs
import time
from .utils.exceptions import pageCheckError
from selenium.common.exceptions import TimeoutException

###############################################################################
def is_valid_reg(driver):
    time.sleep(3)
    try:
        old_url = driver.current_url
        #check page errors before registration  
        page_errors = check_page_errors(driver)
        if page_errors:
            raise pageCheckError(driver.current_url, page_errors)
            
        register_button = get_register_button(driver) 
        register(driver, register_button)
         
        return True
    
    #TimeoutException indicated invalid registraion    
    except TimeoutException as e:                   
        if is_422_status_code(driver):
            #if 422 status registration OK!
            return True
        else:
            return False
    finally:
        driver.get(old_url)
        clear_browser_error_logs(driver)
        
###############################################################################
