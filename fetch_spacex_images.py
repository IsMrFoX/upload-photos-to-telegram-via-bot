import requests
import os
from urllib.parse import urlparse
import argparse


def download_images(url, pathname):

    if not os.path.isdir(pathname):
        os.makedirs(pathname)

    url_parsed_name = urlparse(url).path[len(urlparse(url).path)//2:]

    filename = os.path.join(pathname, f'space_{url_parsed_name}')

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def check_spacex_url(launch_id):

    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'

    response = requests.get(url)
    response.raise_for_status()

    if response.json()['links']['flickr']['original']:
        for link in response.json()['links']['flickr']['original']:
            download_images(link, pathname='images')
    else:
        if response.json()['links']['patch']['small']:
            download_images(response.json()['links']['patch']['small'], pathname='images')
        else:
            print('В этом запуске нет фото')


def main():

    latest_launch_url = 'https://api.spacexdata.com/v5/launches/latest'

    parser = argparse.ArgumentParser(
            description='Программа скачивает имеющиеся картинки по айди запуска.'
    )
    parser.add_argument(
            'url_id',
            help='Введите айди запуска.'
    )
    args = parser.parse_args()

    try:
        check_spacex_url(args.url_id)
    except requests.exceptions.HTTPError:
        print("Введен неправильный 'id' запуска, скачивание картинок происходит из последнего запуска.")
        response = requests.get(latest_launch_url)
        response.raise_for_status()
        if response.json()['links']['flickr']['original']:
            for link in response.json()['links']['flickr']['original']:
                download_images(link, pathname='images')
        else:
            if response.json()['links']['patch']['small']:
                download_images(response.json()['links']['patch']['small'], pathname='images')
            else:
                print('В этом запуске нет фото')


if __name__ == "__main__":
    main()
