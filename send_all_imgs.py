import os
import argparse
import time
import random
import telegram
from download_tools import unpake_photos
from download_tools import send_pictures


def main(images):

    tg_channel_id = os.getenv('TG_CHANNEL_ID')
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(token=telegram_bot_token)

    parser = argparse.ArgumentParser(
        description='Программа выкладывает определенное количество картинок через определенное количество времени.'
                    'Если картинки закончились, перемешивает их и запускает все по новой уже с имеющимися данными '
                    'о количестве картинок и промежутке времени.'
    )
    parser.add_argument(
        'count',
        nargs='?',
        type=int,
        help='Введите число картинок для отправки в телеграм канал.',
        default=1
    )
    parser.add_argument(
        'time',
        nargs='?',
        type=int,
        help='Введите число через которое будут публиковаться картники,'
             ', по умолчанию выставлено раз в 4 часа.',
        default=4
    )
    parser.add_argument(
        'params',
        nargs='?',
        type=str,
        help='Введите параметр измерения времени: "s", "m", "h"',
        default='h'
    )

    args = parser.parse_args()

    while True:
        for index, image in enumerate(images, 1):
            send_pictures(image, bot, tg_channel_id)
            if index % args.count == 0:
                if args.params == 's':
                    time.sleep(args.time)
                elif args.params == 'm':
                    time.sleep(args.time * 60)
                elif args.params == 'h':
                    time.sleep(args.time * 3600)
                else:
                    time.sleep(args.time)
            elif index == len(images):
                break
        random.shuffle(images)
        main(images)


if __name__ == "__main__":
    succsec = False
    while not succsec:
        try:
            main(unpake_photos())
            succsec = True
        except telegram.error.NetworkError:
            time.sleep(10)
