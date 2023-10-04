from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators

class TestClickingOnConstructor:

    def test_transition_by_clicking_on_constructor(self, driver, user_credentials):
        email, password = user_credentials
        driver.find_element(*locators.Locators.LOGIN_TAB).click()
        driver.find_element(*locators.Locators.Email).send_keys(email)
        driver.find_element(*locators.Locators.PASSWORD).send_keys(password)
        driver.find_element(*locators.Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.ORDER_BUTTON)))
        driver.find_element(*locators.Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.SAVE_BUTTON)))
        driver.find_element(*locators.Locators.DESIGNER_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.ORDER_BUTTON)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_click_on_the_stellar_burgers_logo(self, driver, user_credentials):
        email, password = user_credentials
        driver.find_element(*locators.Locators.LOGIN_TAB).click()
        driver.find_element(*locators.Locators.Email).send_keys(email)
        driver.find_element(*locators.Locators.PASSWORD).send_keys(password)
        driver.find_element(*locators.Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable((locators.Locators.ORDER_BUTTON)))
        driver.find_element(*locators.Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable((locators.Locators.SAVE_BUTTON)))
        driver.find_element(*locators.Locators.LOGO_BUTTON).click()
        WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable((locators.Locators.ORDER_BUTTON)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
