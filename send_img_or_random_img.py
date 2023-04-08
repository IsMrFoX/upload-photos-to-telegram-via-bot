import os
import argparse
import telegram
import random
from download_tools import unpake_photos
from download_tools import send_pictures
from dotenv import load_dotenv


def main(images):
    load_dotenv()
    tg_channel_id = os.environ['TG_CHANNEL_ID']
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    bot = telegram.Bot(token=telegram_bot_token)

    parser = argparse.ArgumentParser(
            description='Программа выкладывает определенную картинку, если картинки нет или неверно введена, будет'
                        'выложена случайная картинка из имеющихся. '
    )
    parser.add_argument(
            'image',
            nargs='?',
            help='Введите название картинки.',
            default=random.choice(images)
    )
    args = parser.parse_args()
    image = args.image

    if image in images:
        send_pictures(image=image, bot=bot, tg_channel_id=tg_channel_id)

    else:
        send_pictures(image=random.choice(images), bot=bot, tg_channel_id=tg_channel_id)


if __name__ == "__main__":
    main(unpake_photos())
