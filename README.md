# Task-28.1
Итоговый проект по автоматизации тестирования

Объект тестирования: https://b2c.passport.rt.ru


Для взаимодействия необходимо скопировать репозиторий и установить библиотеки следующей командой в терминале:

pip install -r requirements.txt


Для запуска тестов через терминал по авторизации:
# python -m pytest -v --driver Chrome --driver-path chromedriver.exe tests\test_auth_page.py
