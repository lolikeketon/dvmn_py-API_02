from os import environ
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv
import argparse

def shorten_link(token, url):
    payload = {
        'access_token': token,
        'v': 5.199,
        'url': url
    }

    short_api_url = 'https://api.vk.ru/method/utils.getShortLink'

    response = requests.get(short_api_url, params=payload)
    response.raise_for_status()

    return response.json()


def count_clicks(token, url):
    payload = {
        'access_token': token,
        'v': 5.199,
        'key': urlparse(url).path[1:7],
        'interval': 'forever'
    }

    stats_api_url = 'https://api.vk.ru/method/utils.getLinkStats'

    response = requests.get(stats_api_url, params=payload)
    response.raise_for_status()

    return response.json()


def is_shorten_link(token, url):
    payload = {
        'access_token': token,
        'v': 5.199,
        'key': urlparse(url).path[1:7]
    }

    check_api_url = 'https://api.vk.ru/method/utils.getLinkStats'

    response = requests.get(check_api_url, params=payload)
    response.raise_for_status()

    return not 'error' in response.json()


def main():
    load_dotenv()

    vk_token = environ['VK_TOKEN']

    parser = argparse.ArgumentParser(description='Сокращает вашу ссылку, если ссылка сокращена, показывает количество переходов по ней')

    parser.add_argument('link', help='Ваша ссылка')
    args = parser.parse_args()

    user_url = args.link

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
