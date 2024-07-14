# Регистрация (registration):
# для поиска поля "Имя" по XPATH
registration_name = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
# для поиска поля  "Email" по XPATH
registration_email = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
# для поиска поля  "Пароль" по XPATH
registration_password = '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input'
# для поиска кнопки "Зарегистрироваться" по XPATH
registration_button = '//*[@id="root"]/div/main/div/form/button'
register_error_messange = '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p'

# Логин (login):
# для поиска поля  "Email" по XPATH
login_email = '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
# для поиска поля  "Пароль" по XPATH
login_password = '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
#кнопка войти
login_submit_button = '//*[@id="root"]/div/main/div/form/button'
main_make_order_button = '//*[@id="root"]/div/main/section[2]/div/button'
# для поиска кнопки «Войти в аккаунт» на главной странице по XPATH
main_login_button = '//*[@id="root"]/div/main/section[2]/div/button'
# для поиска кнопки  «Личный кабинет» по XPATH
main_account_profile = '//*[@id="root"]/div/header/nav/a/p'
# для поиска кнопки в форме регистрации по XPATH
login_registration = '//*[@id="root"]/div/main/div/div/p/a'
# для поиска кнопки в форме восстановления пароля по XPATH
login_recover_password = '//*[@id="root"]/div/main/div/div/p/a'

# Личный кабинет (account_profile):
# для поиска кнопки перехода в личный кабинет по XPATH
account_profile_button = '//*[@id="root"]/div/header/nav/a/p'

# Переход в конструктор (costructor):
# для поиска кнопки "Конструктор" по XPATH
constructor_button = '//*[@id="root"]/div/header/nav/ul/li[1]/a'
# для поиска логотипа "Stellar Burgers" по XPATH
stellar_burgers_logo = '//*[@id="root"]/div/header/nav/div/a'

# Выход из личного кабинета (logout):
# для поиска кнопки выхода по XPATH
logout_button = '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'

# Переход по разделам конструктора (constructor_sections):
# для поиска раздела Булки по XPATH
constructor_section_bun = '//*[@id="root"]/div/main/section[1]/div[1]/div[1]/span'
# для поиска раздела Соусы по XPATH
constructor_section_sauce = '//*[@id="root"]/div/main/section[1]/div[1]/div[2]/span'
# для поиска раздела Начинки по XPATH
constructor_section_filling = '//*[@id="root"]/div/main/section[1]/div[1]/div[3]/span'
# для поиска названия раздела Соусы
sause_logo = '//*[@id="root"]/div/main/section[1]/div[2]/h2[2]'
# для поиска названия раздела Булки
bun_logo = '//*[@id="root"]/div/main/section[1]/div[2]/h2[1]'
# для поиска названия раздела Начинки
filling_logo = '//*[@id="root"]/div/main/section[1]/div[2]/h2[3]'

