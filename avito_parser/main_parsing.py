import requests
from math import ceil
from bs4 import BeautifulSoup, SoupStrainer


# THE USELESS PRICE SEARCHER....
def market_choice(market):
    """ Marketplace choice.
    Right now is redundant.
    """
    # TODO: expand this if possible
    marketplaces = {
                    'Avito': 'https://www.avito.ru/moskva?',
                   }
    if not market:
        print('Error in marketplace')
    return marketplaces[market]


def search_item(search_term):
    """ Function to work with user inputted search phrase """
    if not search_term:
        print('Error in search')
        # TODO: Should be an error here
    if ' ' in search_term:
        search_term = search_term.replace(' ', '+')
    return search_term


# Leave it here in case of multiple markets
def amount_of_item(items):
    """ Basically tells how much items per page is there """
    items = ceil(items/50)
    return items


def url_making(market_url, search_term, items):
    """ Make up a url check if it's working """
    URL = str(market_url + f'p={items}&q={search_term}')
    try:
        page = requests.get(URL, timeout=5)
        # print("Page status code:", page.status_code)
        page.raise_for_status()
        # TODO: test for status codes
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)
    return page


def soup_making(market_url, search_term, items):
    """ Making a soup to collect data """
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
            # Maybe here i just take values and check elsewhere?
            if value.isnumeric():
                price_list.append(int(value))
    return price_list


def price_range(prices):
    """ Set price limits """
    min_range, max_range = prices
    if not min_range:
        min_range = 0
    if not max_range:
        # How to make infinite?
        max_range = 999999999
    return min_range, max_range


def delete_extremes(price_list, prices):
    """ If search is too far away from average
    it is probably some other item.
    This function is made in attempt to show only
    items that user actually looked for and not
    the ones that contain search keyword.
    """
    price_list = sorted(price_list)
    min_index = 0
    max_index = len(price_list)
    # Sorting by set boundaries
    for i in price_list:
        if i >= prices[0]:
            break
        else:
            min_index = price_list.index(i)
    for i in price_list[::-1]:
        if i <= prices[1]:
            break
        else:
            max_index = price_list.index(i)
    price_list = price_list[min_index+1:max_index]
    # Do i even need it after setting price boundaries?
    # m = price_list[len(price_list)//2]
    # for price in price_list[:]:
    #     if not (m*0.5) <= price <= (m*1.5):
    #         price_list.remove(price)
    return price_list


def average_price(price_list):
    # Maybe i don't even need it
    return sum(price_list)/len(price_list)


def main_parsing(search_term, items, prices, market='Avito'):
    # Getting data
    market_url = market_choice(market)
    search_term = search_item(search_term)
    prices = price_range(prices)
    items = amount_of_item(items)

    price_list = soup_making(market_url, search_term, items)
    price_list = delete_extremes(price_list, prices)
    return price_list



'''
Вводишь товар, сколько его проанализировать (сомнительная опция)
Получаешь эверадж и вводишь прайс-рэндж
По итогам получаешь 3 самых дешевых и 3 самых дорогих с ссылками?
'''