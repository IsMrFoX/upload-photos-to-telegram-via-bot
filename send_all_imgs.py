import os
import argparse
import time
import random
import telegram


def send_imgs(images):

    test_channel_id = os.getenv('TEST_CHANNEL_ID')
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(token=telegram_bot_token)

    parser = argparse.ArgumentParser(
        description='Программа выкладывает определенное количество картинок через определенное количество времени.'
                    'Если картинки закончились, перемешивает их и запускает все по новой уже с имеющимися данными '
                    'о количестве картинок и промежутке времени.'
    )
    parser.add_argument(
        'count',
        help='Введите количество картинок для отправки в телеграм канал.'
    )
    parser.add_argument(
        'minutes',
        nargs='?',
        help='Введите количество минут, через которое будут публиковаться картники,'
             ' по умолчанию выставлено раз в 4 часа.',
        default=240 * 60
    )
    args = parser.parse_args()

    # number = int(input())

    while True:
        for index, image in enumerate(images, 1):
            bot.send_document(chat_id=test_channel_id,
                              document=open(f'images/{image}', 'rb'))
            if index % int(args.count) == 0:
                time.sleep(args.minutes * 60)
            elif index == len(images):
                time.sleep(args.minutes * 60)
                break
        random.shuffle(images)
        send_imgs(images)


if __name__ == "__main__":
    imgs = os.walk("images")
    for item in imgs:
        imgs = item[2]
    send_imgs(imgs)
