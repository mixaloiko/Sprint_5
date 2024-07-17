from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import urls


# Переход по кнопке "Конструктор"
def test_open_constructor_from_profile_by_constructor_button(driver, account_profile):
    account_profile()
    WebDriverWait(driver, 3).until(expected_conditions.url_contains('account/profile'))
    # Переход в конструктор
    driver.find_element(By.XPATH, locators.constructor_button).click()
    # Ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_matches(urls.main_page))
    # Проверка перехода в конструктор
    assert driver.current_url == urls.main_page


# Переход по логотипу "Stellar Burgers"
def test_open_constructor_from_profile_by_burgers_logo(driver, account_profile):
    account_profile()
    WebDriverWait(driver, 3).until(expected_conditions.url_contains('account/profile'))
    # Переход в конструктор
    driver.find_element(By.CSS_SELECTOR, locators.stellar_burgers_logo).click()
    # Ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_matches(urls.main_page))
    # Проверка перехода в конструктор
    assert driver.current_url == urls.main_page
