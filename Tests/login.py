from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


def fill_in_form_and_log_in(url, xpath):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element(By.XPATH, xpath).click()
    # ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_contains('login'))
    # заполнить форму логина
    driver.find_element(By.XPATH, locators.login_email).send_keys('olga_mikhalkevich_11_123@yandex.ru')
    driver.find_element(By.XPATH, locators.login_password).send_keys('123456789')
    driver.find_element(By.XPATH, locators.login_submit_button).click()
    # ожидание загрузки страницы
    driver.implicitly_wait(3)
    # проверка логина
    make_order_button = None
    try:
        make_order_button = driver.find_element(By.XPATH, locators.main_make_order_button)
    except:
        pass
    finally:
        assert make_order_button is not None and make_order_button.text == 'Оформить заказ'
    # закрыть браузер
    driver.quit()


# вход по кнопке "Войти в аккаунт" на главной странице
fill_in_form_and_log_in('https://stellarburgers.nomoreparties.site/', locators.main_login_button)

# вход через кнопку «Личный кабинет»
fill_in_form_and_log_in('https://stellarburgers.nomoreparties.site/', locators.main_account_profile)

# вход через кнопку в форме регистрации
fill_in_form_and_log_in('https://stellarburgers.nomoreparties.site/register', locators.login_registration)

# вход через кнопку в форме восстановления пароля
fill_in_form_and_log_in('https://stellarburgers.nomoreparties.site/forgot-password', locators.login_recover_password)




