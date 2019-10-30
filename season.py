#!/bin/python3

import sys
from jikanpy import Jikan
from termcolor import colored
from pprint import pprint

jikan = Jikan()
arg = sys.argv[1]


def search(todo):
    items_crop = todo['anime'][:30]
    for each in items_crop:
        if each.get('type') == 'OVA' or each.get('type') == 'Special':
            continue
        else:
            genres = []
            for items in each['genres']:
                genres.append(items['name'])
            if each.get('synopsis') != '(No synopsis yet.)':
                print(colored('Name:', 'green'), each['title'])
                print('')
                print(colored('Genres: ', 'green'), end='')
                for items in genres:
                    print(colored(items + ' ', 'red'), end='')
                
                print('')
                print(colored('MAL link:', 'green'), colored(each['url'], 'blue'))
                print('')
                print(colored('Description: ', 'green'), each['synopsis'])
                print('-' * 80)


if arg == 'upcoming':
    upcoming = jikan.season_later()
    search(upcoming)
else:
    split = arg.split('-')
    try:
        year = int(split[0])
    except ValueError:
        print('The given argument is not valid!\nEXP: 2016-winter')
        exit()

    seasons = ['winter', 'spring', 'fall', 'summer']
    if split[1] not in seasons:
        print('No such a season!!')
        exit()

    search = jikan.season(year=year, season=split[1])
    pprint(search)
