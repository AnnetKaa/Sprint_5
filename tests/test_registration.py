from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_successful_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    #ввод имени
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys('ann')
    #ввод эл.почты
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys('levina0123456@mail.ru')
    #ввод пароля
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys('password123')
    #кнопка зарегистрироваться
    driver.find_element(By.XPATH, ".//main/div/form/button[text()='Зарегистрироваться']").click()
    #кнопка войти
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//main/div/form/button[text()='Войти']")))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    driver.quit()

def test_incorrect_password():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    #ввод имени
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys('ann')
    #ввод эл.почты
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys('annlevina1@mail.ru')
    #ввод пароля
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys('123')
    #кнопка зарегистрироваться
    driver.find_element(By.CLASS_NAME, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa").click()
    #сообщение о некорркетном пароле
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "input__error.text_type_main-default")))

    assert driver.find_element(By.XPATH, './/fieldset[3]/div/p').text == 'Некорректный пароль'

    driver.quit()

def test_empty_name():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    #ввод эл.почты
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input').send_keys('levina012345@mail.ru')
    #ввод пароля
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input').send_keys('password123')
    #кнопка зарегистрироваться
    driver.find_element(By.XPATH, ".//main/div/form/button[text()='Зарегистрироваться']").click()
    #кнопка зарегистрироваться
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//main/div/form/button[text()='Зарегистрироваться']")))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"

    driver.quit()