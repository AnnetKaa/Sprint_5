from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators

class TestConstructor:

    def test_transitions_in_the_constructor_sauces(self, driver):
        driver.find_element(*locators.Locators.SAUSES_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((locators.Locators.SPICY)))
        element = driver.find_element(*locators.Locators.SAUSES_BUTTON_PARENT)

        assert element.get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_transitions_in_the_constructor_fillings(self, driver):
        driver.find_element(*locators.Locators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((locators.Locators.CHOP_BUTTON)))
        element = driver.find_element(*locators.Locators.FILLINGS_BUTTON_PARENT)

        assert element.get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

    def test_transitions_in_the_constructor_buns(self, driver):
        driver.find_element(*locators.Locators.FILLINGS_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((locators.Locators.CHOP_BUTTON)))
        driver.find_element(*locators.Locators.BOOKLET_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((locators.Locators.FLUORESENT_BUN)))
        element = driver.find_element(*locators.Locators.BOOKLET_BUTTON_PARENT)

        assert element.get_attribute('class') == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

