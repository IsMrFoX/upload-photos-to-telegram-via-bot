import requests
import os
from urllib.parse import urlparse
import argparse
from download_tools import download_images
from download_tools import search_images


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


def main():

    latest_launch_url = 'https://api.spacexdata.com/v5/launches/latest'

    parser = argparse.ArgumentParser(
            description='Программа скачивает имеющиеся картинки по айди запуска.'
    )
    parser.add_argument(
            'url_id',
            nargs='?',
            help='Введите айди запуска.',
            default='latest'
    )
    args = parser.parse_args()

    try:
        check_spacex_url(args.url_id)
    except requests.exceptions.HTTPError:
        print("Введен неправильный 'id' запуска, скачивание картинок происходит из последнего запуска.")
        response = requests.get(latest_launch_url)
        response.raise_for_status()
        file_json = response.json()
        orig_imgs = file_json['links']['flickr']['original']
        small_img = file_json['links']['patch']['small']

        if search_images(orig_imgs=orig_imgs, small_img=small_img):
            download_images(orig_imgs, pathname='images')
        else:
            download_images(small_img, pathname='images')


if __name__ == "__main__":
    main()
