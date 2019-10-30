#!/bin/python3

import sys
import os
import inquirer
import requests
import re
from bs4 import BeautifulSoup
import takeanime_url

anime_name = sys.argv[1].replace(' ', '+')


main_url= takeanime_url.tak_anime() + "/?s="
req_url = main_url + anime_name
header= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0'}
req = requests.get(req_url, headers=header).text
soup = BeautifulSoup(req, "html.parser")


pages = []
for pages in soup.findAll('a', attrs={'class': 'page-numbers'}):
    pages.append(pages['href'])


# Remove persian words
pages = [elements.encode('ascii', errors='ignore').decode() for elements in pages]

# Remove empty elements from list
pages = [x for x in pages if x != ' ']


soups = []
soups.append(soup)
for posts in pages:
    req = requests.get(posts, headers=header).text
    soup = BeautifulSoup(req, "html.parser")
    soups.append(soup)



anime_titles = []
anime_links = []
for soup in soups:
    for posts in soup.findAll('div', attrs={'class': 'post_main'}):
        anime_titles.append(posts.find('a')['title'])
        anime_links.append(posts.find('a')['href'])


# Remove persian Words
anime_titles = [elements.encode('ascii', errors='ignore').decode() for elements in anime_titles]


# Fixing the spaces before lists' elements
pattern = '^\s*'
for items in anime_titles:
    anime_titles[anime_titles.index(items)] = re.sub(pattern, '', items)


titles = [inquirer.List('Titles', message="Titles I've found: ", choices=anime_titles)]
answer = inquirer.prompt(titles)
download = answer['Titles']


index = anime_titles.index(download)
req = requests.get(anime_links[index], headers=header).text
soup = BeautifulSoup(req, "html.parser")

homedir = os.path.expanduser("~")
    
f = open(homedir + '/.gnunime/links', 'w')
pattern = 'href=[\'"]?([^\'" >]+.mkv|mp4)'
for items in re.findall(pattern, str(soup)):
    if "trainbit.com" not in items:
        f.write(items)
        f.write('\n')
