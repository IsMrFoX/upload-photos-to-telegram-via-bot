import requests
import os
from urllib.parse import urlparse
import argparse
from download_tools import download_images


def check_spacex_url(launch_id):

    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'

    response = requests.get(url)
    response.raise_for_status()
    file_json = response.json()

    if file_json['links']['flickr']['original']:
        for link in file_json['links']['flickr']['original']:
            download_images(link, pathname='images')
    else:
        if file_json['links']['patch']['small']:
            download_images(file_json['links']['patch']['small'], pathname='images')


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
        if file_json['links']['flickr']['original']:
            for link in file_json['links']['flickr']['original']:
                download_images(link, pathname='images')
        else:
            if file_json['links']['patch']['small']:
                download_images(file_json['links']['patch']['small'], pathname='images')
            else:
                print('В этом запуске нет фото')


if __name__ == "__main__":
    main()
