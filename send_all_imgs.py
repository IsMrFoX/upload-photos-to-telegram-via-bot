import os
import argparse
import time
import random
import telegram
from pathlib import Path
from download_tools import unpake_photos
from download_tools import send_pictures


def main(tg_channel_id, bot, images):
    parser = argparse.ArgumentParser(
        description='Программа выкладывает определенное количество картинок через определенное количество времени.'
                    'Если картинки закончились, перемешивает их и запускает все по новой уже с имеющимися данными '
                    'о количестве картинок и промежутке времени.'
    )
    parser.add_argument(
        'count',
        nargs='?',
        help='Введите количество картинок для отправки в телеграм канал.',
        default=1
    )
    parser.add_argument(
        'minutes',
        nargs='?',
        help='Введите количество минут, через которое будут публиковаться картники,'
             ' по умолчанию выставлено раз в 4 часа.',
        default=240 * 60
    )
    args = parser.parse_args()

       while True:
        for index, image in enumerate(images, 1):
            send_pictures(image, bot, tg_channel_id)
            if index % args.count == 0:
                if args.time[-1] == 's':
                    time.sleep(int(args.time[:-1]))
                elif args.time[-1] == 'm':
                    time.sleep(int(args.time[:-1]) * 60)
                elif args.time[-1] == 'h':
                    time.sleep(int(args.time[:-1]) * 3600)
            elif index == len(images):
                time.sleep(args.time[:-1])
                break
        random.shuffle(images)
        main(images)


if __name__ == "__main__":

    tg_channel_id = os.environ['TG_CHANNEL_ID']
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    bot = telegram.Bot(token=telegram_bot_token)

    success = False
    while not success:
        try:
            main(bot=bot, tg_channel_id=tg_channel_id, images=unpake_photos())
            success = True
        except telegram.error.NetworkError:
            pass
