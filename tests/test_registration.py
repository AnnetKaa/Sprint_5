from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import data

faker = Faker()

class TestRegistration:

    def test_successful_registration(self, driver):
        email = faker.email()
        driver.find_element(*locators.Locators.LOGIN_TAB).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.LOGIN_BUTTON)))
        driver.find_element(*locators.Locators.REG_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.REGISTER_BUTTON)))
        driver.find_element(*locators.Locators.NAME_REG).send_keys(*data.Data.name)
        driver.find_element(*locators.Locators.Email_REG).send_keys(email)
        driver.find_element(*locators.Locators.PASSWORD).send_keys(*data.Data.password)
        driver.find_element(*locators.Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((locators.Locators.LOGIN_BUTTON)))
        driver.find_element(*locators.Locators.Email).send_keys(email)
        driver.find_element(*locators.Locators.PASSWORD).send_keys(*data.Data.password)
        driver.find_element(*locators.Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable((locators.Locators.ORDER_BUTTON)))
        driver.find_element(*locators.Locators.PERSONAL_AREA).click()
        WebDriverWait(driver, 7).until(
            expected_conditions.element_to_be_clickable((locators.Locators.SAVE_BUTTON)))

        assert driver.find_element(*locators.Locators.INFO).text == 'В этом разделе вы можете изменить свои персональные данные'

    def test_incorrect_password(self, driver):
        email = faker.email()
        driver.find_element(*locators.Locators.LOGIN_TAB).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.LOGIN_BUTTON)))
        driver.find_element(*locators.Locators.REG_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.REGISTER_BUTTON)))
        driver.find_element(*locators.Locators.NAME_REG).send_keys(*data.Data.name)
        driver.find_element(*locators.Locators.Email_REG).send_keys(email)
        driver.find_element(*locators.Locators.PASSWORD).send_keys('123')
        driver.find_element(*locators.Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.Locators.INCORRECT_PASSWORD)))

        assert driver.find_element(*locators.Locators.INCORRECT_PASSWORD).text == 'Некорректный пароль'

    def test_empty_name(self, driver):
        email = faker.email()
        driver.find_element(*locators.Locators.LOGIN_TAB).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.LOGIN_BUTTON)))
        driver.find_element(*locators.Locators.REG_BUTTON).click()
        WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((locators.Locators.REGISTER_BUTTON)))
        driver.find_element(*locators.Locators.Email_REG).send_keys(email)
        driver.find_element(*locators.Locators.PASSWORD).send_keys(*data.Data.password)
        driver.find_element(*locators.Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((locators.Locators.REGISTER_BUTTON)))

        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"