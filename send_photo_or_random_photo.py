import os
import argparse
import telegram
import random
from download_tools import unpack_photos
from download_tools import send_photo
from dotenv import load_dotenv


def main():
    photos = unpack_photos()
    load_dotenv()
    tg_channel_id = os.environ['TG_CHANNEL_ID']
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    bot = telegram.Bot(token=telegram_bot_token)

    parser = argparse.ArgumentParser(
            description='Программа выкладывает определенную фотографию, если фотографии нет или неверно введена, будет'
                        'выложена случайная фотография из имеющихся. '
    )
    parser.add_argument(
            'photo',
            nargs='?',
            help='Введите название фотографии.',
            default=random.choice(photos)
    )
    args = parser.parse_args()

    photo = args.photo if args.photo in photos else random.choice(photos)
    send_photo(photo=photo, bot=bot, tg_channel_id=tg_channel_id)


if __name__ == "__main__":
    main()
