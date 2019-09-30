import requests
import html5lib
from bs4 import BeautifulSoup
import time

URL = "https:\\\\www.github.com\\nehal31"
URL = "https://github.com"

page = requests.get(url=URL)
print(page.status_code)
print("-" * 50)
print(page.text)
print("-" * 50)
print(page.content)



