#!/bin/python3
import requests
from bs4 import BeautifulSoup

def tak_anime():
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    google_search = "https://www.google.com/search?client=firefox-b-d&q=%D8%AA%DA%A9+%D8%A7%D9%86%DB%8C%D9%85%D9%87"
    req = requests.get(google_search, headers=header)
    soup = BeautifulSoup(req.text, "html.parser")
    return (soup.find('cite').text)

