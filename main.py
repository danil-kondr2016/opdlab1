from bs4 import BeautifulSoup
import requests

url = "https://auto.drom.ru"

page = requests.get(url)
if page.status_code != 200:
    print("Error")
    exit(-1)

dom = BeautifulSoup(page.text, "html.parser")
div = dom.find('div', class_='eqhdpot0')
imgs = div.findAll('img')

cars = set(x["alt"] for x in imgs if x["alt"] != '')
with open('cars.txt', 'w') as file:
    print(*cars, file=file, sep='\n')