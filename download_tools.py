import requests
import os
from urllib.parse import urlparse


def download_images(urls, params='', pathname='images'):

    if not os.path.isdir(pathname):
        os.makedirs(pathname)

    if isinstance(urls, list):
        for link in urls:
            if link is not None:
                url_parsed_name = urlparse(link).path.split('/')[-1]
                filename = os.path.join(pathname, url_parsed_name)

                response = requests.get(link, params=params)
                response.raise_for_status()

                with open(filename, 'wb') as file:
                    file.write(response.content)

    elif isinstance(urls, str):
        url_parsed_name = urlparse(urls).path.split('/')[-1]
        filename = os.path.join(pathname, url_parsed_name)

        response = requests.get(urls, params=params)
        response.raise_for_status()

        with open(filename, 'wb') as file:
            file.write(response.content)


def unpake_photos():

    imgs = os.walk("images")
    for items in imgs:
        imgs = items[2]

    return imgs
