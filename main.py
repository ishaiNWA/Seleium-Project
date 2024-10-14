from src.utils.site_selenium_utils import setup_driver, extract_language_urls, fill_lang_forms,  check_page_errors
from src.reg_checker import is_valid_reg
from src.utils.telegram_bot import send_telegram_alarm
from src.exceptions import pageCheckError
from src.utils.loggers import registration_error_logger , page_errors_logger, internal_error_logger
import traceback



###############################################################################

def site_reg_check(base_page_url):
    try:
        driver = setup_driver()
        if driver is None:
            internal_error_logger.error("Failed to set up WebDriver. NordVPN connection may have failed.")
            return  # Exit the function if driver setup failed

        driver.get(base_page_url)
        page_errors = check_page_errors(driver)
        if page_errors:
            handle_page_check_errors(base_page_url , page_errors)
             # Exit the function if base_url_has errors
            return 
        
        lang_map = extract_language_urls(driver)
        for lang_code , lang_page_url in lang_map.items():
            print(f"{lang_code}-{lang_page_url}")
            driver.get(lang_page_url)
            fill_lang_forms(driver)
            try:
                    # test if valid registration
                    if not is_valid_reg(driver):
                        registration_error_logger.error(f"failed to register from {driver.current_url}") 
                        send_telegram_alarm(f"failed to register from {driver.current_url}")
            except pageCheckError as e:
                    handle_page_check_errors(e.current_url ,e.errors )
                    traceback.print_exc()
                    
            except Exception as e:
                    handle_generic_exception(driver.current_url , e)
                
                    
    except Exception as e:
        handle_generic_exception(driver.current_url , e)
    finally:
        driver.quit()
    
    send_telegram_alarm(f"system has finished registration cheking for {base_page_url}")        
    
    
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
    url_to_check = "https://immediatfolex.ai/"
    site_reg_check(url_to_check) 

if __name__=="__main__":
    main()