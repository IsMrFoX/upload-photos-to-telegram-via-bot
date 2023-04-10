# Space Telegram


### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
------------------------------
### Как работать со скриптами

#### 1. fetch_space_apod_photos --> скачивает введенное количество фотографий в директорию 'images', по умолчанию скачивается одна фотография.

Для него потребуется api_token c [api.nasa/apod](https://api.nasa.gov/#apod), выбираем  *'Generate API Key'*, вводим данные, получаем токен. 
Переменная окружения для токена - *"NASA_TOKEN"*, ее необходимо положить в созданный вами файл ".env".
Запускаем оболочку PowerShell или открыть командную строку и в ней запустить скрипт (ввести путь до файла, ввести запуск виртуального окружения, имя файла,  количество фотографий для скачивания).

    >>> C:\Scripts\pipenv run python fetch_space_apod_photos.py 5 

#### 2. fetch_space_epic_photos --> cкачивает последние эпик фотографии в директорию 'images'

Необязательная переменная окружения для токена - *"NASA_TOKEN"*
Для него потребуется просто его запустить(через виртуальное окружение, можно ввести свой токен, смотри №1 чтобы получить Токен):

     >>> C:\Scripts\pipenv run python fetch_space_epic_photos.py 
    
#### 3. fetch_spacex_photos --> скачивает фотографии по 'id' запуска, в ином случае качает из последнего запуска.

Для него потребуется просто его запустить(через виртуальное окружение) и ввести 'id' запуска:

     >>> C:\Scripts\pipenv run python fetch_spacex_photos.py 5eb87d47ffd86e000604b38a
     
#### 4. send_photo_or_random_photo --> выкладывает в телеграм канал введенную фотографию из имеющихся, либо выкладывает случайную из скачанных фотографий.

Для него потребуется телеграм-бот-токен [как зарегестрировать бота](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html) (пример токена: 958423683:AAEAtJ5Lde5YYfkjergber). Переменная окружения для бот-токена *"TELEGRAM_BOT_TOKEN"*.
Также потребуется 'id' телеграм канала, куда бот будет отправлять наши фотографии. Узнать ваш 'id' канала можно переслав любое сообщение из нужного нам канала --> телеграм боту 
:[бот для получения id канала](https://t.me/getmyid_bot), 3-тья строчка 'id' нужного нам канала. Переменная окружения для него *'TG_CHANNEL_ID'*. Далее:

    >>> C:\Scripts\pipenv run python send_photo_or_random_photo.py RocketLaunch_Jiang_4199.jpg

#### 5. send_all_photos --> выкладывает в телеграм канал все фотографии в бесконечном цикле с задаваемым числом и временным промежутком

Переменные окружения: *'TG_CHANNEL_ID'* - для телеграм канала, и *'TELEGRAM_BOT_TOKEN'* - для бот токена. 1. Аргумент - сколько фотографий выкладывать, по умолчанию 1 фотография. 2. Аргумент - Через сколько минут выложить следующие (**в минутах**),.
Если все фотографии выложены, то программа перемешивает их и продолжает работать заново. По умолчанию выставлено выкладывать фотографии раз в 4 часа.

    >>> C:\Scripts\pipenv run python send_all_photos.py 5 60

-------------------------
### Виртуальное окружение

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html?highlight=venv#module-venv), или как в моем случае [pyenv](https://docs.python-guide.org/dev/virtualenvs/) для изоляции проекта.

----------------
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
