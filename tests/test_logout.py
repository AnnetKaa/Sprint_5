from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
def test_logout(user_credentials):
    email, password = user_credentials
    driver.get("https://stellarburgers.nomoreparties.site/")
    #кнопка личный кабинет
    driver.find_element(By.XPATH, ".//main/section[2]/div/button").click()
    #ввести эл.почту
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(email)
    #ввести пароль
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(password)
    #кнопка войти
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click()
    #кнопка оформить заказ
    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//main/section[2]/div/button")))
    #кнопка личный кабинет
    driver.find_element(By.XPATH, ".//body/div/div/header/nav/a/p").click()
    #кнопка оформить заказ
    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//main/div/div/div/div/button[2]")))
    #кнопка выход
    driver.find_element(By.XPATH, ".//main/div/nav/ul/li[3]/button").click()
    #кнопка войти
    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//main/div/form/button")))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    driver.quit()
