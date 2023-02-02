import argparse
import datetime
import requests
from download_tools import download_images


def fetch_epic_url(api_token):

    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {
        'api_key': f'{api_token}'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    file_json = response.json()
    date_time = datetime.datetime.fromisoformat
    urls = []
    image_dates = []
    image_names = []
    part_link = "https://api.nasa.gov/EPIC/archive/natural/"

    for item in file_json:
        image_dates.append(
            str(date_time(item['date']).date()).replace('-', '/')
        )

    for item in file_json:
        image_names.append(item['image'])

    for index, data in enumerate(image_dates):
        urls.append(
            f"{part_link}{data}/png/{image_names[index]}.png"
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
