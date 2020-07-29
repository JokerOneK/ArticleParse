from bs4 import BeautifulSoup
from urllib.request import *

url = 'https://vk.com/@yvkurse-muzeinyi-kompleks-tolbuhino'

def get_html():
    request = Request(url)
    html = urlopen(request).read()
    return html

def main():
    opener =

main()