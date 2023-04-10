import os
import argparse
import time
import random
import telegram
from download_tools import unpack_photos
from download_tools import send_photo
from dotenv import load_dotenv


def main():
    load_dotenv()
    images = unpack_photos()
    tg_channel_id = os.environ['TG_CHANNEL_ID']
    telegram_bot_token = os.environ['TELEGRAM_BOT_TOKEN']
    bot = telegram.Bot(token=telegram_bot_token)

    parser = argparse.ArgumentParser(
        description='Программа выкладывает определенное количество фотографий через определенное количество времени.'
                    'Если фотографии закончились, перемешивает их и запускает все по новой уже с имеющимися данными '
                    'о количестве фотографий и промежутке времени.'
    )
    parser.add_argument(
        'count',
        nargs='?',
        type=int,
        help='Введите число фотографий для отправки в телеграм канал.',
        default=1
    )
    parser.add_argument(
        'time',
        nargs='?',
        type=int,
        help='Введите число через которое будут публиковаться фоторграфии,'
             ', по умолчанию выставлено раз в 4 часа.',
        default=4 * 3600
    )

    args = parser.parse_args()
    if args.count == 0:
        print("Неверный ввод, нельзя выкладывать 0 фотографий")
    else:
        while True:
            for index, photo in enumerate(images, 1):
                try:
                    send_photo(
                            photo,
                            bot,
                            tg_channel_id,
                        )
                except telegram.error.NetworkError:
                    time.sleep(10)

                if args.count == index:
                    time.sleep(args.time * 60)

            random.shuffle(images)


if __name__ == "__main__":
    main()
