from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random
import locators


# тест с корректными данными
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")
random_int = random.randint(100, 999)
# заполнить форму регистрации:
driver.find_element(By.XPATH, locators.registration_name).send_keys('Olga')
driver.find_element(By.XPATH, locators.registration_email).send_keys(f'olga_mikhalkevich_11_{random_int}@yandex.ru')
driver.find_element(By.XPATH, locators.registration_password).send_keys('123456789')
driver.find_element(By.XPATH, locators.registration_button).click()

# ожидание загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.url_contains('login'))

# проверить, что произошел переход на страницу входа
current_url = driver.current_url
assert 'login' in current_url
# закрыть браузер
driver.quit()


# Тест с некорректным паролем
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")
random_int = random.randint(100, 999)

# заполнить форму регистрации:
driver.find_element(By.XPATH, locators.registration_name).send_keys('Olga')
driver.find_element(By.XPATH, locators.registration_email).send_keys(f'olga_mikhalkevich_11_{random_int}@yandex.ru')
driver.find_element(By.XPATH, locators.registration_password).send_keys('12345')
driver.find_element(By.XPATH, locators.registration_button).click()

# ожидание загрузки страницы
WebDriverWait(driver, 1)

# проверяем появляется ли сообщение об ошибке и текст сообщения
error_message = None
try:
    error_message = driver.find_element(By.XPATH, locators.register_error_messange)
except:
    pass
finally:
    assert error_message is not None and error_message.text == 'Некорректный пароль'

# закрыть браузер
driver.quit()
