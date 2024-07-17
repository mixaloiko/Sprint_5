from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locators
import urls


# тест перехода в раздел Соусы
def test_constructor_section_sauce(driver):
    driver.get(urls.main_page)
    # Найти кнопку раздела "Соусы"
    driver.find_element(By.CSS_SELECTOR, locators.constructor_section_sauce).click()
    # ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.sause_logo)))
    # проверить что раздел с соусами отображается
    element = driver.find_element(By.XPATH, locators.sause_logo)
    assert element.is_displayed()


# тест перехода в раздел Булки
def test_constructor_section_bun(driver):
    driver.get(urls.main_page)
    # Найти кнопку раздела "Соусы"
    driver.find_element(By.CSS_SELECTOR, locators.constructor_section_sauce).click()
    # Найти кнопку раздела "Булки"
    driver.find_element(By.CSS_SELECTOR, locators.constructor_section_bun).click()
    # ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.bun_logo)))
    # проверить что раздел с булками отображается
    element = driver.find_element(By.XPATH, locators.bun_logo)
    assert element.is_displayed()


# тест перехода в раздел Начинки
def test_constructor_section_fillings(driver):
    driver.get(urls.main_page)
    # Найти кнопку раздела "Начинки"
    driver.find_element(By.CSS_SELECTOR, locators.constructor_section_filling).click()
    # ожидание загрузки страницы
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.filling_logo)))
    # проверить что раздел с начинками отображается
    element = driver.find_element(By.XPATH, locators.filling_logo)
    assert element.is_displayed()
