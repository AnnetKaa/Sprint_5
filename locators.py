from selenium.webdriver.common.by import By

class Locators:
    LOGIN_TAB = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    Email = (By.XPATH, ".//input[@name='name']")
    PASSWORD = (By.XPATH, ".//input[@name = 'Пароль']")
    LOGIN_BUTTON = (By.XPATH, ".//button[text() = 'Войти']")
    LOGIN_VIA_REG = (By.XPATH, ".//a[text() = 'Войти']")
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    PERSONAL_AREA = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    SAVE_BUTTON = (By.XPATH, ".//button[text() = 'Сохранить']")
    EXIT_BUTTON = (By.XPATH, ".//button[text() = 'Выход']")
    DESIGNER_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")
    LOGO_BUTTON = (By.XPATH, ".//div[@class = 'AppHeader_header__logo__2D0X2']")
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    NAME_REG = (By.XPATH, ".//fieldset[1]/div/div/input[@name = 'name']")
    Email_REG = (By.XPATH, ".//fieldset[2]/div/div/input[@name = 'name']")
    REG_BUTTON = (By.XPATH, ".//a[text()='Зарегистрироваться']")