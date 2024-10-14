
from selenium.webdriver.common.by import By

class PageElements:
    LANGUAGE_MENU = (By.ID, "menu-item-wpml-ls-13-en-sub-menu")
    FIRST_NAME = (By.ID, "form-first_name")
    LAST_NAME = (By.ID, "form-last_name")
    EMAIL = (By.ID, "form-email")
    REGISTER_BUTTON = (By.ID, "optInForm-btn")
    COUNTRY_CONTAINER = (By.CLASS_NAME, "iti__flag-container")
    GB_OPTION = (By.ID, "iti-0__item-gb-preferred")
    PHONE_NUMBER = (By.ID, "form-phone_number")
    SUBMMIT_CREDENTIAL_BUTTON = (By.ID, "optInForm-btn")
    REDIRECT_BUTTON = (By.ID, "form-btn")



""""

def setup_driver():
 
     # Connect to NordVPN UK server
    server = "UK" 
        try:
            print(f"Attempting to connect to NordVPN server: {server}")
            result = subprocess.run(["nordvpn", "connect", server], capture_output=True, text=True, check=True)
            print("NordVPN connection attempt completed")
            print("Stdout:", result.stdout)
            print("Stderr:", result.stderr)
            break  # If successful, exit the loop
        except subprocess.CalledProcessError as e:
            print(f"Failed to connect to NordVPN server {server}. Error:")
            print("Stdout:", e.stdout)
            print("Stderr:", e.stderr)
            print("Return code:", e.returncode)
    else:
        print("Failed to connect to any NordVPN server")
        return None

        # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # creates a Service object, which is used to define how the WebDriver 
    # should start and stop the browser driver process.
    service = Service(ChromeDriverManager().install())
    # creates an instance of the Chrome WebDriver. allowing interaction with a browser
    return  webdriver.Chrome(service=service, options=chrome_options)

"""
