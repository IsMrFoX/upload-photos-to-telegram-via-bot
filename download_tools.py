import requests
import os
from urllib.parse import urlparse
from pathlib import Path


def download_images(urls, params='', pathname='images'):

    if not os.path.isdir(pathname):
        os.makedirs(pathname)

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


def check_spacex_url(launch_id):

    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'

    response = requests.get(url)
    response.raise_for_status()
    file_json = response.json()
    orig_imgs = file_json['links']['flickr']['original']
    small_img = file_json['links']['patch']['small']

    if search_images(orig_imgs=orig_imgs, small_img=small_img):
        download_images(orig_imgs, pathname='images')
    else:
        download_images(small_img, pathname='images')
