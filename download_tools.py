import requests
import os
from urllib.parse import urlparse
from pathlib import Path


def download_images(urls, params='', pathname='images'):

    if not os.path.isdir(pathname):
        os.makedirs(pathname)

    if isinstance(urls, list):
        save_images(urls, params, pathname)

    elif isinstance(urls, str):
        save_image(urls, params, pathname)


def save_images(urls, params='', pathname='images'):

    for link in urls:
        if link is not None:
            url_parsed_name = urlparse(link).path.split('/')[-1]
            filename = os.path.join(pathname, url_parsed_name)

            response = requests.get(link, params=params)
            response.raise_for_status()

            with open(filename, 'wb') as file:
                file.write(response.content)


def save_image(url, params='', pathname='images'):

    url_parsed_name = urlparse(url).path.split('/')[-1]
    filename = os.path.join(pathname, url_parsed_name)

    response = requests.get(url, params=params)
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

