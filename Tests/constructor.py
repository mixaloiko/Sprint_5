from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


def open_constructor_from_profile(button_xpath):
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Найти кнопку перехода в личный кабинет
    driver.find_element(By.XPATH, locators.account_profile_button).click()

    # ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_contains('login'))

    # заполнить форму логина
    driver.find_element(By.XPATH, locators.login_email).send_keys(
        'olga_mikhalkevich_11_123@yandex.ru')
    driver.find_element(By.XPATH, locators.login_password).send_keys('123456789')
    driver.find_element(By.XPATH, locators.login_submit_button).click()

    # ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_matches('https://stellarburgers.nomoreparties.site/'))

    # Найти кнопку перехода в личный кабинет
    driver.find_element(By.XPATH, locators.account_profile_button).click()

    # ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_contains('account/profile'))

    # Переход в конструктор
    driver.find_element(By.XPATH, button_xpath).click()

    # Ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_matches('https://stellarburgers.nomoreparties.site/'))

    # Проверка перехода в конструктор
    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    # Закрыть браузер
    driver.quit()

# Переход по кнопке "Конструктор"
open_constructor_from_profile(locators.constructor_button)

# Переход по логотипу "Stellar Burgers"
open_constructor_from_profile(locators.stellar_burgers_logo)