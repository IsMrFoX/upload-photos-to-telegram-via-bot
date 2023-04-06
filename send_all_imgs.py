import os
import argparse
import time
import random
import telegram
from download_tools import unpake_photos
from download_tools import send_pictures


def sleep(index, count, amount_time, time_value, images):
    if index % count == 0:
        if time_value == 's':
            time.sleep(amount_time)
        elif time_value == 'm':
            time.sleep(amount_time * 60)
        elif time_value == 'h':
            time.sleep(amount_time * 3600)
        elif index == len(images):
            time.sleep(amount_time * 60)


def main(images):
    tg_channel_id = os.environ['TG_CHANNEL_ID']
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
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
            sleep(index=index,
                  count=args.count,
                  amount_time=args.time,
                  time_value=args.params,
                  images=images
                  )

        random.shuffle(images)


if __name__ == "__main__":
    success = False
    while not success:
        try:
            main(unpake_photos())
            success = True
        except telegram.error.NetworkError:
            time.sleep(10)
