from .utils.site_selenium_utils import  get_redirect_button, redirect_page, check_page_errors
import time
from .exceptions import pageCheckError
from selenium.common.exceptions import TimeoutException

###############################################################################

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
