from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators


# тест с корректными данными
def test_register_correct_data(driver, register):
    register(123456789)
    # ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.url_contains('login'))
    # проверить, что произошел переход на страницу входа
    current_url = driver.current_url
    assert 'login' in current_url


# Тест с некорректным паролем
def test_register_incorrect_password(driver, register):
    register(12345)
    # ожидание загрузки страницы
    WebDriverWait(driver, 1)
    # проверяем появляется ли сообщение об ошибке и текст сообщения
    error_message = None
    try:
        error_message = driver.find_element(By.CSS_SELECTOR, locators.register_error_message)
    except:
        pass
    finally:
        assert error_message is not None and error_message.text == 'Некорректный пароль'
