from selenium.webdriver.common.by import By

import locators
import urls


def assert_login_successful(driver):
    # проверка логина
    make_order_button = None
    try:
        make_order_button = driver.find_element(By.CSS_SELECTOR, locators.main_make_order_button)
    except:
        pass
    finally:
        assert make_order_button is not None and make_order_button.text == 'Оформить заказ'


# вход через кнопку логина на главной странице
def test_login_by_login_button_on_main_page(driver, login):
    driver.get(urls.main_page)
    driver.find_element(By.CSS_SELECTOR, locators.main_login_button).click()
    login()
    assert_login_successful(driver)


# вход через кнопку «Личный кабинет»
def test_login_by_account_profile_button_on_main_page(driver, login):
    driver.get(urls.main_page)
    driver.find_element(By.XPATH, locators.account_profile_button).click()
    login()
    assert_login_successful(driver)


# вход через кнопку в форме регистрации
def test_login_by_login_button_on_registration_page(driver, login):
    driver.get(urls.register_page)
    driver.find_element(By.LINK_TEXT, locators.login_registration).click()
    login()
    assert_login_successful(driver)


# вход через кнопку в форме восстановления пароля
def test_login_by_login_button_on_recover_password_page(driver, login):
    driver.get(urls.forgot_password_page)
    driver.find_element(By.LINK_TEXT, locators.login_recover_password).click()
    login()
    assert_login_successful(driver)
