import requests
import os
from urllib.parse import urlparse
from pathlib import Path


def download_photos(urls, params=None, pathname='photos'):

    os.makedirs(pathname, exist_ok=True)

    if isinstance(urls, list):
        for link in urls:
            if link is not None:
                save_photo(link, params, pathname)

    elif isinstance(urls, str):
        save_photo(urls, params, pathname)


def save_photo(link, params='', pathname='photos'):

    url_parsed_name = urlparse(link).path.split('/')[-1]
    filename = os.path.join(pathname, url_parsed_name)

    response = requests.get(link, params=params)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def unpake_photos():
    imgs = os.walk("photos")
    for items in imgs:
        imgs = items[2]

    return imgs


def has_photos(orig_imgs, small_img):
    if orig_imgs:
        return True
    else:
        if small_img:
            return False


def send_photo(photo, bot, tg_channel_id):
    with open(Path.cwd() / 'photos' / f'{photo}', "rb") as file:
        bot.send_document(chat_id=tg_channel_id,
                          document=file)
