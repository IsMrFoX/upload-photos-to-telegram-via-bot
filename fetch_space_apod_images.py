import requests
import os
from urllib.parse import urlparse
import argparse


def download_images(urls, pathname):

    if not os.path.isdir(pathname):
        os.makedirs(pathname)

    for link in urls:
        url_parsed_name = urlparse(link).path.split('/')[-1]
        filename = os.path.join(pathname, url_parsed_name)

        response = requests.get(link)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response.content)


def fetch_apod_urls(url, params):

    response = requests.get(url, params=params)
    response.raise_for_status()
    urls = []

    for count in range(len(response.json())):
        urls.append(response.json()[count].get('hdurl'))
    return urls


def main():

    apod_api_token = os.getenv('API_TOKEN')
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
        'api_key': f'{apod_api_token}',
        'count': f'{args.count}'
    }
    apod_url = "https://api.nasa.gov/planetary/apod"

    try:
        imgs_urls = fetch_apod_urls(apod_url, params)
    except requests.exceptions.HTTPError:
        print("Неверно введено число картинок, проверьте ваш ввод и попробуйте еще раз.")
    else:
        download_images(imgs_urls, pathname='images')


if __name__ == "__main__":
    main()

