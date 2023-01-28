# Space Telegram


### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
------------------------------
### Как работать со скриптами

#### 1. fetch_space_apod_images --> скачивает введенное количество картинок в директорию 'images', по умолчанию скачивается одна картинка.

Для него потребуется API_TOKEN c [api.nasa/apod](https://api.nasa.gov/#apod), выбираем  *'Generate API Key'*, вводим данные, получаем токен. 
Переменная окружения для токена - *"apod_api_token"*, ее необходимо положить в созданный вами файл ".env".
Запускаем оболочку PowerShell или открыть командную строку и в ней запустить скрипт (ввести путь до файла, ввести запуск виртуального окружения, имя файла,  количество картинок для скачивания).

    >>> C:\Scripts\pipenv run python fetch_space_apod_images.py 5 

#### 2. fetch_space_epic_images --> cкачивает последние эпик картинки в директорию 'images'

Для него потребуется просто его запустить(через виртуальное окружение, также можно ввести свой токен):

     >>> C:\Scripts\pipenv run python fetch_space_epic_images.py (ваш токен, либо оставьте пустым)
    
#### 3. fetch_spacex_images --> скачивает картинки по 'id' запуска, в ином случае качает из последнего запуска.

Для него потребуется просто его запустить(через виртуальное окружение) и ввести 'id' запуска:

     >>> C:\Scripts\pipenv run python fetch_spacex_images.py 5eb87d47ffd86e000604b38a
     
#### 4. send_img_or_random_img --> выкладывает в телеграм канал введенную картинку из имеющихся, либо выкладывает случайную из скачаных картинок.

Для него потребуется телеграм-бот-токен [как регестрировать бота](https://way23.ru/%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0-%D0%B2-telegram.html) (пример токена: 958423683:AAEAtJ5Lde5YYfkjergber). Переменная окружения для бот-токена *'telegram_bot_token'*.
Его необходимо вставить в переменную *'bot=...(token=telegram_bot_token)'*. Также потребуется 'id' телеграм канала, куда бот будет отправлять наши файлы. Узнать ваш 'id' канала можно переслав любое сообщение из нужного нам канала --> телеграм боту 
:[бот для получения id канала](https://t.me/getmyid_bot), 3-тья строчка 'id' нужного нам канала. Переменная окружения для него *'tg_channel_id'*. Далее:

    >>> C:\Scripts\pipenv run python send_img_or_random_img.py RocketLaunch_Jiang_4199.jpg

#### 5. send_all_imgs --> выкладывает в телеграм канал все картинки в бесконечном цикле с задаваемым числом и временным промежутком(в минутах)

Переменные окружения те же, что и в №4. 1. Аргумент - сколько картинок выкладывать, по умолчанию 1 картинка. 2. Аргумент - Через сколько минут выложить следующие, по умолчанию выставлено раз в 4 часа. 
Если все картинки выложены, то программа перемешивает картинки и продолжает работать.

    >>> C:\Scripts\pipenv run python send_all_imgs.py 5 5

-------------------------
### Виртуальное окружение

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html?highlight=venv#module-venv), или как в моем случае [pyenv](https://docs.python-guide.org/dev/virtualenvs/) для изоляции проекта.

----------------
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
