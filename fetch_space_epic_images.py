import requests
import os
from urllib.parse import urlparse
import argparse
import datetime
import telegram


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


def fetch_epic_url():

    url = "https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY"
    response = requests.get(url)
    response.raise_for_status()

    date_time = datetime.datetime.fromisoformat
    urls = []

    for item in response.json():
        urls.append(
            f"https://api.nasa.gov/EPIC/archive/natural/"
            f"{str(date_time(item['date']).date()).replace('-','/')}/png/{item['image']}.png?api_key=DEMO_KEY"
        )
    return urls


def main():

    parser = argparse.ArgumentParser(
        description='Программа скачивает последние эпик картинки планеты Земля.'
        'Программа имеет ограниченное количество запросов для скачивания картинок.'
        'После исчерпания лимита, попробуйте позже.')

    args = parser.parse_args()

    try:
        img_urls = fetch_epic_url()
    except requests.exceptions.HTTPError:
        print("Достигнут лимит для скачивания картинок, попробуйте позже.")
    else:
        download_images(img_urls, pathname='images')


if __name__ == "__main__":
    main()
