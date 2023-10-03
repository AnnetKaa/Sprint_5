from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
def test_login_using_the_log_in_to_your_account(user_credentials):
    driver = webdriver.Chrome()
    email, password = user_credentials
    driver.get("https://stellarburgers.nomoreparties.site/")
    #кнопка войти в аккаунт
    driver.find_element(By.XPATH, ".//main/section[2]/div/button").click()
    #ввести эл.почту
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(email)
    #ввести пароль
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(password)
    #кнопка войти
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click()
    #оформить заказ
    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//main/section[2]/div/button")))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()

def test_login_via_the_button_in_the_registration_form(user_credentials):
    driver = webdriver.Chrome()
    email, password = user_credentials
    driver.get("https://stellarburgers.nomoreparties.site/register")
    #кнопка войти
    driver.find_element(By.XPATH,".//main/div/div/p/a").click()
    #кнопка войти
    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//main/div/form/button")))
    #ввести эл.почту
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(email)
    #ввести пароль
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(password)
    #кнопка войти
    driver.find_element(By.XPATH, ".//main/div/form/button").click()
    #кнопка оформить заказ
    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//main/section[2]/div/button")))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()

def test_login_through_the_personal_Account_button(user_credentials):
    driver = webdriver.Chrome()
    email, password = user_credentials
    driver.get("https://stellarburgers.nomoreparties.site/")
    #кнопка личный кабинет
    driver.find_element(By.XPATH, ".//header/nav/a/p").click()
    #ввод эл. почты
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(email)
    #ввод пароля
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys(password)
    #кнопка вход
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click()
    #кнопка оформить заказ
    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//main/section[2]/div/button")))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()