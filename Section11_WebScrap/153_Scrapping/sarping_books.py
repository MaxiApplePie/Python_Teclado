import requests
from bs4 import BeautifulSoup

page = requests.get('http://example.com')
# print(page.content)

parser = BeautifulSoup(page.content, 'html.parser')
print(parser.find('h1').string)
