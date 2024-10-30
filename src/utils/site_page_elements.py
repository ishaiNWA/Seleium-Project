
from selenium.webdriver.common.by import By

class PageElements:
    LANGUAGE_MENU = (By.ID, "menu-item-wpml-ls-13-en-sub-menu")
    FIRST_NAME = (By.ID, "form-first_name")
    LAST_NAME = (By.ID, "form-last_name")
    EMAIL = (By.ID, "form-email")
    COUNTRY_CONTAINER = (By.CLASS_NAME, "iti__flag-container")
    GB_OPTION = (By.ID, "iti-0__item-gb-preferred")
    PHONE_NUMBER = (By.ID, "form-phone_number")
    SUBMMIT_CREDENTIAL_BUTTON = (By.ID, "optInForm-btn")
    REGISTER_BUTTON = (By.ID, "form-btn")

