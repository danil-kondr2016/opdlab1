from bs4 import BeautifulSoup
import requests


def get_cars(url):
    page = requests.get(url)
    if page.status_code != 200:
        raise Exception(f"HTTP error {page.status_code}")

    dom = BeautifulSoup(page.text, "html.parser")
    divs = dom.findAll('a', attrs={'data-ftid': 'bulls-list_bull'})

    cars = set()

    for div in divs:
        link = div["href"]
        title_dom = div.find('span', attrs={"data-ftid": "bull_title"})
        descriptions_dom = div.findAll('span', attrs={"data-ftid": "bull_description-item"})

        descriptions = []
        for description in descriptions_dom:
            descriptions.append(description.text.replace('<!-- -->', ''))

        cars.add((link, title_dom.text, ''.join(descriptions)))

    return cars


def write_cars(cars, file):
    for link, title, description in cars:
        print(link, title, description, sep=';', file=file)
