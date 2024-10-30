from src.utils.site_selenium_utils import setup_driver, extract_language_urls, fill_reg_form,  check_page_errors
from src.reg_checker import is_valid_reg
from src.utils.telegram_bot import send_telegram_alarm
from src.exceptions import pageCheckError
from src.utils.loggers import registration_error_logger , page_errors_logger, internal_error_logger
import traceback

###############################################################################
def sites_reg_check(sites_url_list):
    
    driver = None
    try:
        try:
            driver = setup_driver()
        except Exception as e:
            internal_error_logger.error("Failed to set up WebDriver.")
            return  # Exit the function if driver setup failed
            
        #checking  registrations for each site
        for site_url in sites_url_list:
            driver.get(site_url)
            page_errors = check_page_errors(driver)
            if page_errors:
                handle_page_check_errors(site_url , page_errors)
                continue
            
            lang_map = extract_language_urls(driver)
            #checking registrations for each language
            for lang_code , lang_page_url in lang_map.items():
                print(f"{lang_code}-{lang_page_url}")
                driver.get(lang_page_url)
                fill_reg_form(driver)                    
                try:
                    if not is_valid_reg(driver):
                        handle_registration_error(driver.current_url)
                        break
                except pageCheckError as e:
                    handle_page_check_errors(e.current_url ,e.errors)
                    break
                except Exception as e:
                    handle_generic_exception(driver.current_url , e)
                    break
                        
            send_telegram_alarm(f"system has finished registration cheking for {site_url}")
                                            
    except Exception as e:
        handle_generic_exception(driver.current_url , e)
    finally:
        if driver:
            driver.quit()
        
###############################################################################
def handle_registration_error(page_url):
     registration_error_logger.error(f"failed to register from {page_url}") 
     send_telegram_alarm(f"failed to register from {page_url}")
     
###############################################################################
def handle_page_check_errors(page_url , errors):
    print(f"Page check errors in url : {page_url}:")
    page_errors_logger.error(f"Page error in url: {page_url}\n errors: {errors}")
    send_telegram_alarm(f"Page check errors in url : {page_url}:")   
    
###############################################################################
def handle_generic_exception(page_url ,e):
    print(f"generic exception in url : {page_url}:")
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {str(e)}")
    internal_error_logger.error(f"generic exception was thrown at{page_url}\n exception: {e}")
    error_message = f"An error occurred: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
    print(error_message)  # This will print to console
    internal_error_logger.error(error_message)  # This will log to your error log file
    send_telegram_alarm(f"generic exception was thrown at : {page_url}:")
    
###############################################################################   
def main():
    
    
    url_list = [ "https://immediatfolex.ai/" ,
                 "https://immediatfolex.ai/" ,
                "https://immediatfolex.ai/"]
   
    sites_reg_check(url_list) 

if __name__=="__main__":
    main()

###############################################################################

#TODO clean all code. 
#TODO try to handle dependancies
#TODO rearainge files, delete usless files
#TODO write read me file