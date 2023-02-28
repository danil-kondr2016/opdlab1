from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import json

url = "https://auto.drom.ru"

page = requests.get(url)
if page.status_code != 200:
    print("Error")
    exit(-1)

dom = BeautifulSoup(page.text, "html.parser")
imgs = dom.findAll('img')

cars = set()
for x in imgs:
    cars.add(x["alt"])

cars = set(x["alt"] for x in imgs if x["alt"] != '')
print(*cars, sep='\n')