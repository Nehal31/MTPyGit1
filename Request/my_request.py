import requests as r
import html5lib
from bs4 import BeautifulSoup

URL="https://httpbin.org"
URL_YOUTUBE = "https://www.youtube.com/"
URL_GOOGLE="https://www.google.com"

page = r.get(URL_GOOGLE)
soup = BeautifulSoup(page.content, 'html5lib')


print(soup)


