import requests
import argparse
from download_tools import search_images
from download_tools import download_images
from dotenv import load_dotenv


def download_spacex_imgs(launch_id):

    url = f'https://api.spacexdata.com/v5/launches/{launch_id}'

    response = requests.get(url)
    response.raise_for_status()
    files = response.json()
    orig_imgs = files['links']['flickr']['original']
    small_img = files['links']['patch']['small']

    if search_images(orig_imgs=orig_imgs, small_img=small_img):
        download_images(orig_imgs, pathname='images')
    else:
        download_images(small_img, pathname='images')


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
            description='Программа скачивает имеющиеся картинки по айди запуска.'
    )
    parser.add_argument(
            'launch_id',
            nargs='?',
            help='Введите айди запуска.',
            default='latest'
    )
    args = parser.parse_args()

    try:
        download_spacex_imgs(args.launch_id)
    except requests.exceptions.HTTPError:
        print("Введен неправильный 'id' запуска, скачивание картинок происходит из последнего запуска.")
        download_spacex_imgs(launch_id='latest')


if __name__ == "__main__":
    main()
