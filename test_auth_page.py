# для запуска тестов через терминал:
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_auth_page.py


def test_guest_can_go_to_login_page(browser):
    link = "https://b2c.passport.rt.ru"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# тестирование авторизации через почту
def test_auth_page(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    page.enter_email("kryuchkova96@yandex.ru")
    page.enter_password("B2U-tHH-wtR-Lfx")
    page.click_btn()

 # тестирование авторизации через номер телефона
 def test_auth_page(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    page.enter_numberphone("+7-996-963-93-15")
    page.enter_password("B2U-tHH-wtR-Lfx")
    page.click_btn()

 # тестирование авторизации через некорректный номер телефона
 def test_auth_page(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    page.enter_numberphone("+7-999-000-00-00")
    page.enter_password("B2U-tHH-wtR-Lfx")
    page.click_btn()

# тестирование авторизации через некорректный e-mail
def test_auth_page(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    page.enter_email("autissan200@yandex.ru")
    page.enter_password("B2U-tHH-wtR-Lfx")
    page.click_btn()

# тестирование авторизации через верную почту и неверный пароль
def test_auth_page(selenium):
    page = AuthPage(selenium)
    time.sleep(3)
    page.enter_email("kryuchkova96@yandex.ru")
    page.enter_password("B2U-tHH-wtR-Lfx")
    page.click_btn()

# проверка, что клик на Ростелеком в хэдере ведет другую страницу
    p = Rostelecom(selenium)
    url_before = p.driver.current_url
    p.logo_header_click()
    url_after = p.driver.current_url
    assert url_before != url_after, "Клик на Ростелеком в хэдере не ведет на другую страницу"

# проверка, что клик на "Выйти" в хэдере ведет на страницу регистрации
# создаем объект класса страницы со всеми животными
    p = Rostelecom(selenium)
    p.log_out_click()
    url_after_click = p.driver.current_url
    assert url_after_click == 'https://b2c.passport.rt.ru', \
    "Клик на кнопку 'Выйти' в хэдере ведет на страницу авторизации"

