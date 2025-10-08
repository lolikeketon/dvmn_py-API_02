from os import environ
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def shorten_link(token, url):
    payload = {
        'access_token': token,
        'v': 5.199,
        'url': url
    }

    url_for_short_link = 'https://api.vk.ru/method/utils.getShortLink'

    response = requests.get(url_for_short_link, params=payload)
    response.raise_for_status()

    return response.json()


def count_clicks(token, url):
    payload = {
        'access_token': token,
        'v': 5.199,
        'key': urlparse(url).path[1:7],
        'interval': 'forever'
    }

    url_for_link_stats = 'https://api.vk.ru/method/utils.getLinkStats'

    response = requests.get(url_for_link_stats, params=payload)
    response.raise_for_status()

    return response.json()


def is_shorten_link(token, url):
    payload = {
        'access_token': token,
        'v': 5.199,
        'key': urlparse(url).path[1:7]
    }

    url_for_link_check = 'https://api.vk.ru/method/utils.getLinkStats'

    response = requests.get(url_for_link_check, params=payload)
    response.raise_for_status()

    return not 'error' in response.json()


def main():
    load_dotenv()

    vk_token = environ['TOKEN_VK']

    user_url = input('Введите ссылку: ')

    if is_shorten_link(vk_token, user_url):
        try:
            stats = count_clicks(vk_token, user_url)
            print('Количество переходов по ссылке:', stats['response']['stats'][0]['views'])
        except KeyError:
            print('Вы ввели не правильную ссылку')
            print(stats['error'])
    else:
        try:
            short = shorten_link(vk_token, user_url)
            print('Сокращённая ссылка:', short['response']['short_url'])
        except KeyError:
            print('Вы ввели не правильную ссылку')
            print(short['error']['error_msg'])


if __name__ == '__main__':
    main()
