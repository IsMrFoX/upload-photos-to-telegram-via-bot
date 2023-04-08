import requests
import os
from urllib.parse import urlparse
from pathlib import Path


def download_images(urls, params=None, pathname='images'):

    os.makedirs(pathname, exist_ok=False)

    if isinstance(urls, list):
        for link in urls:
            if link is not None:
                save_images(link, params, pathname)

    elif isinstance(urls, str):
        save_images(urls, params, pathname)


def save_images(link, params='', pathname='images'):

    url_parsed_name = urlparse(link).path.split('/')[-1]
    filename = os.path.join(pathname, url_parsed_name)

    response = requests.get(link, params=params)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def unpake_photos():
    imgs = os.walk("images")
    for items in imgs:
        imgs = items[2]

    return imgs


def search_images(orig_imgs, small_img):
    if orig_imgs:
        return True
    else:
        if small_img:
            return False


def send_pictures(image, bot, tg_channel_id):
    with open(Path.cwd() / 'images' / f'{image}', "rb") as file:
        bot.send_document(chat_id=tg_channel_id,
                          document=file)
