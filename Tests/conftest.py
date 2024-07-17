import random

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import urls


@pytest.fixture
def driver():
    _driver = Chrome()
    yield _driver
    _driver.quit()


@pytest.fixture
def login(driver):
    def _login():
        # ожидание загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.url_contains('login'))
        # заполнить форму логина
        driver.find_element(By.CSS_SELECTOR, locators.login_email).send_keys('olga_mikhalkevich_11_123@yandex.ru')
        driver.find_element(By.CSS_SELECTOR, locators.login_password).send_keys('123456789')
        driver.find_element(By.CSS_SELECTOR, locators.login_submit_button).click()
        # ожидание загрузки страницы
        driver.implicitly_wait(3)

    return _login


@pytest.fixture
def account_profile(driver, login):
    def _account_profile():
        driver.get(urls.login_page)
        login()
        # ожидание загрузки страницы
        WebDriverWait(driver, 3).until(expected_conditions.url_matches(urls.main_page))
        # Найти кнопку перехода в личный кабинет
        driver.find_element(By.XPATH, locators.account_profile_button).click()
        # ожидание загрузки страницы
        driver.implicitly_wait(3)

    return _account_profile


@pytest.fixture
def register(driver):
    def _register(password):
        driver.get(urls.register_page)
        random_int = random.randint(100, 999)
        # заполнить форму регистрации:
        driver.find_element(By.CSS_SELECTOR, locators.registration_name).send_keys('Olga')
        driver.find_element(By.CSS_SELECTOR, locators.registration_email).send_keys(
            f'olga_mikhalkevich_11_{random_int}@yandex.ru')
        driver.find_element(By.CSS_SELECTOR, locators.registration_password).send_keys(password)
        driver.find_element(By.CSS_SELECTOR, locators.registration_button).click()
        # ожидание загрузки страницы
        driver.implicitly_wait(3)

    return _register
