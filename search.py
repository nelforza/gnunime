#!/bin/python

import sys
import inquirer
from jikanpy import Jikan
from termcolor import colored


jikan = Jikan()

# Searches anime name using Jikan
def anime_name(anime):
    search = jikan.search('anime', anime)
    return search

     
def anime_show(items):
    items_crop = items['results'][:10]

    for each in items_crop:
        if each.get('type') == 'OVA' or each.get('type') == 'Special':
            continue
        else:
            print(colored('Name:', 'green'), each['title'])

            if each.get('type') == 'TV':
                print(colored('Start Date:', 'green'), colored(each['start_date'][:4], 'red'))

                if each.get('end_date') == None:
                    print(colored('End Date:', 'green'), colored('Not finished', 'red'))

                else:
                    print(colored('End Date:', 'green'), colored(each['end_date'][:4], 'red'))

                test = each['episodes']
                if test == 0:
                    pass
                else:
                    print(colored('Episodes:', 'green'), colored(each['episodes'], 'red'))


            elif each.get('type') == 'Movie':
                print(colored('Released on:', 'green'), colored(each['start_date'][:4], 'red'))


            print(colored('Score:', 'green'), colored(each['score'], 'red'))
            print(colored('MAL link:', 'green'), colored(each['url'], 'blue'))
            print('')
            print(colored('Description: ', 'green'), each['synopsis'])
            print('')
            print('-' * 80)


anime = sys.argv[1]
items = anime_name(anime)
anime_show(items)

