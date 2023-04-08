import argparse
import requests
import os
from datetime import datetime
from download_tools import download_images
from dotenv import load_dotenv

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

    for item in files:
        image_names = [item['image']]
        image_dates = [datetime.fromisoformat(item['date']).date()]

    part_data_links = [date.strftime("%Y/%m/%d") for date in image_dates]

    for data, name in zip(part_data_links, image_names):
        urls.append(
            f"{part_link}{data}/png/{name}.png"
        )
    return urls


def main():
    load_dotenv()
    api_token = os.getenv('NASA_TOKEN', default='DEMO_KEY')

    parser = argparse.ArgumentParser(
        description='Программа скачивает последние эпик картинки планеты Земля.'
                    'Программа имеет ограниченное количество запросов для скачивания картинок.'
                    'После исчерпания лимита, попробуйте позже.')

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
