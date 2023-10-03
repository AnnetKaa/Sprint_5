from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_transition_by_clicking_on_constructor(user_credentials):
    email, password = user_credentials
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    # кнопка личный кабинет
    driver.find_element(By.XPATH, ".//main/section[2]/div/button").click()
    #ввести эл.почту
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(email)
    #ввести пароль
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(password)
    # кнопка войти
    driver.find_element(By.CLASS_NAME,"button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click()
    #кнопка оформить заказ
    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//main/section[2]/div/button")))
    # кнопка личный кабинет
    driver.find_element(By.XPATH, ".//body/div/div/header/nav/a/p").click()
    # кнопка сохранить
    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//main/div/div/div/div/button[2]")))
    # кнопка конструктор
    driver.find_element(By.XPATH, ".//header/nav/ul/li[1]/a/p").click()
    # кнопка оформить заказ
    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//main/section[2]/div/button")))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()

def test_click_on_the_stellar_burgers_logo(user_credentials):
    email, password = user_credentials
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    # кнопка личный кабинет
    driver.find_element(By.XPATH, ".//main/section[2]/div/button").click()
    # ввести эл.почту
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(email)
    # ввести пароль)
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(password)
    # кнопка войти
    driver.find_element(By.CLASS_NAME,
                        "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click()
    # кнопка оформить заказ
    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//main/section[2]/div/button")))
    # кнопка личный кабинет
    driver.find_element(By.XPATH, ".//body/div/div/header/nav/a/p").click()
    # кнопка сохранить
    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//main/div/div/div/div/button[2]")))
    # логотип
    driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()
    # кнопка оформить заказ
    WebDriverWait(driver, 7).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//main/section[2]/div/button")))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()
