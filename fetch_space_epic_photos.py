import requests
import os
from datetime import datetime
from download_tools import download_photos
from dotenv import load_dotenv


def fetch_epic_url(api_token):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    params = {
        'api_key': f'{api_token}'
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    files = response.json()
    part_link = "https://api.nasa.gov/EPIC/archive/natural/"

    for item in files:
        photos_names = [item['image']]
        photos_dates = [datetime.fromisoformat(item['date']).date()]

    part_data_links = [date.strftime("%Y/%m/%d") for date in photos_dates]

    urls = [f"{part_link}{date}/png/{name}.png" for date, name in zip(part_data_links, photos_names)]

    return urls


def main():
    load_dotenv()
    api_token = os.getenv('NASA_TOKEN', default='DEMO_KEY')

    url_params = {
        'api_key': f'{api_token}'
    }

    try:
        img_urls = fetch_epic_url(api_token)

    except requests.exceptions.HTTPError:
        print("Введен неверный 'api token'")
    else:
        download_photos(img_urls, url_params, pathname='images')


if __name__ == "__main__":
    main()
