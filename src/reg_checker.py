from .utils.site_selenium_utils import  get_register_button, register, check_page_errors, is_422_status_code, clear_browser_error_logs
import time
from .exceptions import pageCheckError
from selenium.common.exceptions import TimeoutException

###############################################################################
def is_valid_reg(driver):
    time.sleep(3)
    try:
        orig_url = driver.current_url
        #check page errors before registration  
        page_errors = check_page_errors(driver)
        #TODO claer console after each iteration
        
        if page_errors:
            raise pageCheckError(driver.current_url, page_errors)
            
        register_button = get_register_button(driver) 
        register(driver, register_button)
         
        #TODO clearance point???
        return True
        
    except TimeoutException as e:
        print(f"TIME OUT EXCEPTION!!!\nfor {driver.current_url} ")
        #TimeoutException indicated invalid registraion               
        if is_422_status_code(driver):
            #if 422 status registration OK!
            print("422 TRUE")
            return True
        else:
            print("422 FALSE")
            return False
    finally:
        driver.get(orig_url)
        clear_browser_error_logs(driver)
        
###############################################################################
