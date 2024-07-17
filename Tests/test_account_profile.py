from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import urls


def test_open_account_profile(driver, login):
    driver.get(urls.main_page)
    driver.find_element(By.XPATH, locators.account_profile_button).click()
    login()
    # ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_matches(urls.main_page))
    # Найти кнопку перехода в личный кабинет
    driver.find_element(By.XPATH, locators.account_profile_button).click()
    # ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_contains('account/profile'))
    # проверить, что произошел переход на страницу личного кабинета
    current_url = driver.current_url
    assert 'account/profile' in current_url
