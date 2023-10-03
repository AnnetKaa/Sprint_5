import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

def test_transitions_in_the_constructor():
    driver.get("https://stellarburgers.nomoreparties.site/")
    #клик на Соусы
    driver.find_element(By.XPATH, ".//span[text()='Соусы']").click()
    time.sleep(1)
    #клик на Начинки
    driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
    time.sleep(1)
    #клик на Булки
    driver.find_element(By.XPATH, ".//span[text()='Булки']").click()
    time.sleep(1)

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()