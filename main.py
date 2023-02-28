from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import json

url = "https://auto.drom.ru"

page = requests.get(url)
if page.status_code != 200:
    print("Error")
    exit(-1)

dom = BeautifulSoup(page.text, "html.parser")
div = dom.find('div', class_='eqhdpot0')
imgs = div.findAll('img')

cars = set(x["alt"] for x in imgs if x["alt"] != '')
print(*cars, sep='\n')