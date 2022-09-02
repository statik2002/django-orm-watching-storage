# Пульт охраны банка
Первый урок DjangoORM на Devman

## Установка
- Скачать
- Создать виртуальное окружение
- Установить зависимости `pip install -r requirements.txt`
- Запустите сервер командой `python3 main.py`


## Использование

После запуска 'пульт' доступен по адресу: http://127.0.0.1:8000 и состоит из трех cтраниц:
1. Список всех кодов доступа. доступна по адресу http://127.0.0.1:8000/active_passcards
2. Список находящихся в данный момент пользователей в хранилище. Доступна по адресу: http://127.0.0.1:8000/storage_information
3. Список всех визитов каждого владельца доступа. Доступна по адресу: http://127.0.0.1:8000/passcard_info/<uuid:passcode>




