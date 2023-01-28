import os
import argparse
import telegram
import random
from pathlib import Path
from download_tools import unpake_photos

def main(imgs):

    tg_channel_id = os.getenv('TG_CHANNEL_ID')
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(token=telegram_bot_token)

    parser = argparse.ArgumentParser(
            description='Программа выкладывает определенную картинку, если картинки нет или неверно введена, будет'
                        'выложена случайная картинка из имеющихся. '
    )
    parser.add_argument(
            'image',
            nargs='?',
            help='Введите название картинки.',
            default=random.choice(imgs)
    )
    args = parser.parse_args()
    img = args.image

    if img in imgs:
        with open(Path.cwd() / 'images' / f'{img}', 'rb') as file:
            bot.send_document(
                chat_id=tg_channel_id,
                document=file)
    else:
        with open(Path.cwd() / 'images' / f'{random.choice(imgs)}', 'rb') as file:
            bot.send_document(
                chat_id=tg_channel_id,
                document=file)


if __name__ == "__main__":
    main(unpake_photos())

