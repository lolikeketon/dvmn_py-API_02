from os import getenv
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def shorten_link(token, url):
    payload = {
        'access_token': token,
        'v': 5.199,
        'url': url
    }

    work_url = 'https://api.vk.ru/method/utils.getShortLink'

    response = requests.get(work_url, params=payload)
    response.raise_for_status()

    return response.json()


def count_clicks(token, url):
    payload = {
        'access_token': token,
        'v': 5.199,
        'key': urlparse(url).path[1:7],
        'interval': 'forever'
    }

    work_url = 'https://api.vk.ru/method/utils.getLinkStats'

    response = requests.get(work_url, params=payload)
    response.raise_for_status()

    return response.json()


def is_shorten_link(url):
    return urlparse(url).netloc == 'vk.cc'


def main():
    load_dotenv()

    api_vk = getenv('VK_API')

    user_url = input('Введите ссылку: ')

    if is_shorten_link(user_url):
        try:
            stats = count_clicks(api_vk, user_url)
            print('Количество переходов по ссылке:', stats['response']['stats'][0]['views'])
        except KeyError:
            print('Вы ввели не правильную ссылку')
            print(stats['error'])
    else:
        try:
            short = shorten_link(api_vk, user_url)
            print('Сокращённая ссылка:', short['response']['short_url'])
        except KeyError:
            print('Вы ввели не правильную ссылку')
            print(short['error']['error_msg'])


if __name__ == '__main__':
    main()
