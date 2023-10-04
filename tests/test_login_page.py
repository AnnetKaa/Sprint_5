from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators

class TestLogin:
    def test_login_using_the_log_in_to_your_account(self, driver, user_credentials):
        email, password = user_credentials
        driver.find_element(*locators.Locators.LOGIN_TAB).click()
        driver.find_element(*locators.Locators.Email).send_keys(email)
        driver.find_element(*locators.Locators.PASSWORD).send_keys(password)
        driver.find_element(*locators.Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.ORDER_BUTTON)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_via_the_button_in_the_registration_form(self, driver, user_credentials):
        email, password = user_credentials
        driver.find_element(*locators.Locators.LOGIN_TAB).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.LOGIN_BUTTON)))
        driver.find_element(*locators.Locators.REG_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.REGISTER_BUTTON)))
        driver.find_element(*locators.Locators.LOGIN_VIA_REG).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.LOGIN_BUTTON)))
        driver.find_element(*locators.Locators.Email).send_keys(email)
        driver.find_element(*locators.Locators.PASSWORD).send_keys(password)
        driver.find_element(*locators.Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.ORDER_BUTTON)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_login_through_the_personal_Account_button(self, driver, user_credentials):
        email, password = user_credentials
        driver.find_element(*locators.Locators.PERSONAL_AREA).click()
        driver.find_element(*locators.Locators.Email).send_keys(email)
        driver.find_element(*locators.Locators.PASSWORD).send_keys(password)
        driver.find_element(*locators.Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.ORDER_BUTTON)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"