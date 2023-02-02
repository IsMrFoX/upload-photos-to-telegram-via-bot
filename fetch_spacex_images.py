import requests
import argparse
from download_tools import check_spacex_url


def main():

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
        check_spacex_url(args.launch_id)
    except requests.exceptions.HTTPError:
        print("Введен неправильный 'id' запуска, скачивание картинок происходит из последнего запуска.")
        check_spacex_url(launch_id='latest')


if __name__ == "__main__":
    main()
