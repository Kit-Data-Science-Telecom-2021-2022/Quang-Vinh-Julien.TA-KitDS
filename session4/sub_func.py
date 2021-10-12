#%%
import requests
import json
from bs4 import BeautifulSoup

def extract_beer_infos(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    beer_details = soup.find_all(class_="small-12 content-column")[0]
    name = beer_details.find_all(class_="product-detail-info-title")[0].find("h1").text
    note = beer_details.find(class_="stars")['data-percent']
    price = soup.find(class_="price").text.split()[0].replace(',', '.')
    volume = beer_details.find(class_="small-6 medium-9 columns js-beer-volume").text.split()[0]
    infos = {
        'name': name,
        'note': int(note),
        'price': float(price),
        'volume': int(volume),
    }
    return infos