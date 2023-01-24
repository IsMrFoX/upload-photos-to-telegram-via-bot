import os
import argparse
import telegram
import random


def main():

    test_channel_id = os.getenv('TEST_CHANNEL_ID')
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    bot = telegram.Bot(token=telegram_bot_token)

    imgs = os.walk("images")
    for items in imgs:
        imgs = items[2]

    parser = argparse.ArgumentParser(
            description='Программа выкладывает определенную картинку, если картинки нет или неверно введена, будет'
                        'выложена случайная картинка из имеющихся. '
    )
    parser.add_argument(
            'image',
            nargs='?',
            help='Введите  название картинки.',
            default=random.choice(imgs)
    )
    args = parser.parse_args()
    img = args.image

    if img in imgs:
        bot.send_document(
            chat_id=test_channel_id,
            document=open(f'images/{img}', 'rb'))
    else:
        bot.send_document(
            chat_id=test_channel_id,
            document=open(f'images/{random.choice(imgs)}', 'rb'))


if __name__ == 'main':
    main()
