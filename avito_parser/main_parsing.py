import requests
from math import ceil
from statistics import median
from bs4 import BeautifulSoup, SoupStrainer


# THE USELESS PRICE SEARCHER....
# Функция выбора торговой площадки
def market_choice(market):
    # TODO: expand this if possible
    marketplaces = {
                    'Avito': 'https://www.avito.ru/moskva?',
                   }
    if not market:
        print('You are fucked in marketplace')
    return marketplaces[market]


# Функция выбора предмета поиска
def search_item(search_term):
    # For now we consider one word search
    if not search_term:
        print("You're fucked")
        # TODO: Should be an error here
    if ' ' in search_term:
        search_term = search_term.replace(' ', '+')
    return search_term


def amount_of_item(items):
    # Take a limit, divide it by 50 because Avito shows such amount on 1 page
    items = ceil(int(items)/50)
    return items


def url_making(market_url, search_term, items):
    # Make a URL according to chosen marketplace
    # Make a request
    # URL = https://www.avito.ru/moskva?p=num&q=text
    URL = str(market_url + f'p={items}&q={search_term}')
    try:
        page = requests.get(URL, timeout=5)
        # print("Page status code:", page.status_code)
        page.raise_for_status()
        # TODO: test for status codes
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)     # Break soup_making if error
    return page


# Скрейпинг данных с сайта по запросу
def soup_making(market_url, search_term, items):
    # Fill the list
    # Repeat X times
    price_list = []
    # should use clean 'items' in order to
    # set limit in finding tags, make ceiling right here
    for i in range(1, items+1):
        page = url_making(market_url, search_term, i)
        # Do you want to pull all these args through all code?
        price_strainer = SoupStrainer('meta', itemprop='price')
        soup = (
            BeautifulSoup(page.text, 'lxml', parse_only=price_strainer)
        )
        for tag in soup.find_all(True):
            value = tag['content']
            if value.isnumeric():
                price_list.append(int(value))
    return price_list


# WORKING WITH COLLECTED DATA

# Избавляем список от лишних сумм
def delete_extremes(price_list):
    m = median(price_list)
    for price in price_list[:]:
        if not (m*0.5) <= price <= (m*1.5):
            price_list.remove(price)
    return price_list


# Установка пределов суммы
def price_range():
    # Two values to get affordable price
    print("Enter minimum price")
    min_range = input()
    if min_range is None:
        min_range = 0
    print("Enter maximum price")
    max_range = input()
    # check for isnumeric()
    return min_range, max_range


# Подсчет средней цены
def average_price(price_list):
    return sum(price_list)/len(price_list)


# Самый дешевый, самый дорогой товар и ссылка на него
def main_parsing(search_term, items, market='Avito'):
    market_url = market_choice(market)
    search_term = search_item(search_term)
    items = amount_of_item(items)
    price_list = soup_making(market_url, search_term, items)
    price_list = delete_extremes(price_list)
    return price_list
