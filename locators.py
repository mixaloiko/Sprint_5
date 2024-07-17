# Регистрация (registration):
# для поиска поля "Имя" по CSS_SELECTOR
registration_name = '.Auth_form__3qKeq fieldset:nth-child(1) input'
# для поиска поля  "Email" по CSS_SELECTOR
registration_email = '.Auth_form__3qKeq fieldset:nth-child(2) input'
# для поиска поля  "Пароль" по CSS_SELECTOR
registration_password = '.Auth_form__3qKeq fieldset:nth-child(3) input'
# для поиска кнопки "Зарегистрироваться" по CSS_SELECTOR
registration_button = '.Auth_form__3qKeq button'
# для поиска сообщения об ошибке CSS_SELECTOR
register_error_message = '.Auth_form__3qKeq .input__error'

# Логин (login):
# для поиска поля  "Email" по CSS_SELECTOR
login_email = '.Auth_login__3hAey fieldset:nth-child(1) input'
# для поиска поля  "Пароль" по CSS_SELECTOR
login_password = '.Auth_login__3hAey fieldset:nth-child(2) input'
# кнопка войти по CSS_SELECTOR
login_submit_button = '.Auth_login__3hAey button'
# для поиска кнопки оформить заказ по CSS_SELECTOR
main_make_order_button = '.BurgerConstructor_basket__container__2fUl3 button'
# для поиска кнопки «Войти в аккаунт» на главной странице по CSS_SELECTOR
main_login_button = '.BurgerConstructor_basket__container__2fUl3 button'
# для поиска кнопки в форме регистрации по LINK_TEXT
login_registration = 'Войти'
# для поиска кнопки в форме восстановления пароля по LINK_TEXT
login_recover_password = 'Войти'

# Личный кабинет (account_profile):
# для поиска кнопки перехода в личный кабинет по XPATH
account_profile_button = '//*[@id="root"]/div/header/nav/a/p'

# Переход в конструктор (costructor):
# для поиска кнопки "Конструктор" по XPATH
constructor_button = '//*[@id="root"]/div/header/nav/ul/li[1]/a'
# для поиска логотипа "Stellar Burgers" по CSS_SELECTOR
stellar_burgers_logo = '.AppHeader_header__logo__2D0X2 a'

# Выход из личного кабинета (logout):
# для поиска кнопки выхода по XPATH
logout_button = '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'

# Переход по разделам конструктора (constructor_sections):
# для поиска раздела Булки по CSS_SELECTOR
constructor_section_bun = '.BurgerIngredients_ingredients__1N8v2 .tab_tab__1SPyG:nth-child(1) span'
# для поиска раздела Соусы по CSS_SELECTOR
constructor_section_sauce = '.BurgerIngredients_ingredients__1N8v2 .tab_tab__1SPyG:nth-child(2) span'
# для поиска раздела Начинки по CSS_SELECTOR
constructor_section_filling = '.BurgerIngredients_ingredients__1N8v2 .tab_tab__1SPyG:nth-child(3) span'
# для поиска названия раздела Соусы по XPATH
sause_logo = '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]'
# для поиска названия раздела Булки по XPATH
bun_logo = '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]'
# для поиска названия раздела Начинки по XPATH
filling_logo = '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]'

