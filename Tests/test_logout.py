from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import urls


def test_logout(driver, login):
    driver.get(urls.main_page)
    # Найти кнопку перехода в личный кабинет
    driver.find_element(By.XPATH, locators.account_profile_button).click()
    login()
    # ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_matches(urls.main_page))
    # Найти кнопку перехода в личный кабинет
    driver.find_element(By.XPATH, locators.account_profile_button).click()
    # ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_contains('account/profile'))
    # Найти кнопку "Выйти"
    driver.find_element(By.XPATH, locators.logout_button).click()
    # ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_contains('login'))
    # проверить, что произошел переход на страницу входа
    current_url = driver.current_url
    assert 'login' in current_url

