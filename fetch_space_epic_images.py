import argparse
import requests
import os
from datetime import datetime
from download_tools import download_images


def fetch_epic_url(api_token):

    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {
        'api_key': f'{api_token}'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    files = response.json()
    urls = []
    part_link = "https://api.nasa.gov/EPIC/archive/natural/"

    image_names = [item['image'] for item in files]
    image_dates = [datetime.fromisoformat(data['date']).date() for data in files]

    for index, data in enumerate(image_dates):
        urls.append(
            f"{part_link}{str(data).replace('-', '/')}/png/{image_names[index]}.png"
        )
    return urls


def main():

    api_token = os.getenv('NASA_TOKEN', default='DEMO_KEY')

    parser = argparse.ArgumentParser(
        description='Программа скачивает последние эпик картинки планеты Земля.'
        'Программа имеет ограниченное количество запросов для скачивания картинок.'
        'После исчерпания лимита, попробуйте позже.')

    args = parser.parse_args()

    url_params = {
        'api_key': f'{api_token}'
    }

    try:
        img_urls = fetch_epic_url(api_token)

    except requests.exceptions.HTTPError:
        print("Введен неверный 'api token'")
    else:
        download_images(img_urls, url_params, pathname='images')


if __name__ == "__main__":
    main()
