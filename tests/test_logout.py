from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import data

class TestLogout:
    def test_logout(self, driver):
        driver.find_element(*locators.Locators.LOGIN_TAB).click()
        driver.find_element(*locators.Locators.Email).send_keys(*data.Data.email)
        driver.find_element(*locators.Locators.PASSWORD).send_keys(*data.Data.password)
        driver.find_element(*locators.Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.ORDER_BUTTON)))
        driver.find_element(*locators.Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.SAVE_BUTTON)))
        driver.find_element(*locators.Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable((locators.Locators.LOGIN_BUTTON)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
