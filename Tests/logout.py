from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators

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

# Найти кнопку "Выйти"
driver.find_element(By.XPATH, locators.logout_button).click()

# ожидание загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.url_contains('login'))

# проверить, что произошел переход на страницу входа
current_url = driver.current_url
assert 'login' in current_url

#закрыть браузер
driver.quit()
