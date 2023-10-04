from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestConstructor:

    def test_transitions_in_the_constructor_sauces(self, driver):
        driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//img[@alt = 'Соус Spicy-X']")))

        assert driver.find_element(By.XPATH, ".//h2[text()='Соусы']").text == 'Соусы'

    def test_transitions_in_the_constructor_fillings(self, driver):
        driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//img[@alt = 'Говяжий метеорит (отбивная)']")))

        assert driver.find_element(By.XPATH, ".//h2[text()='Начинки']").text == 'Начинки'

    def test_transitions_in_the_constructor_buns(self, driver):
        driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//img[@alt = 'Говяжий метеорит (отбивная)']")))
        driver.find_element(By.XPATH, ".//span[text()='Булки']").click()
        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")))

        assert driver.find_element(By.XPATH, ".//h2[text()='Булки']").text == 'Булки'

