import requests
import os
from urllib.parse import urlparse
import argparse
from download_tools import download_images


def fetch_apod_urls(url, params):

    response = requests.get(url, params=params)
    response.raise_for_status()
    files = response.json()

    urls = [item['hdurl'] for item in files]
    
    return urls


def main():

    api_token = os.environ['NASA_TOKEN']
    parser = argparse.ArgumentParser(
        description='Программа скачивает введенное количество картинок, либо скачивает одну картинку.'
    )
    parser.add_argument(
        'count',
        nargs='?',
        help='Введите количестов картинок для скачивания.',
        default=1
    )
    args = parser.parse_args()
    params = {
        'api_key': f'{api_token}',
        'count': f'{args.count}'
    }
    apod_url = "https://api.nasa.gov/planetary/apod"

    try:
        img_urls = fetch_apod_urls(apod_url, params)
    except requests.exceptions.HTTPError:
        print("Неверно введено число картинок, проверьте ваш ввод и попробуйте еще раз.")
    else:
        download_images(img_urls, pathname='images')


if __name__ == "__main__":
    main()
