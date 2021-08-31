import unittest
from avito_parser import main_parsing

'''
Test list:
1. market_choice
2. search_item
    Enter nothing
    Enter numbers
    Enter two options
    Enter None
    Enter 0
    Enter 1
3. amount_of_items
    Enter 1
    Enter 0
    Enter 50
    Enter 421
    Enter None
    Enter word
    Enter 1000000000
    enter 99999999999999
4. url_making
    Enter invalid url
    Enter error 500 (items = 300)
    Enter wrong search item
'''


class Testing_MarketChoice(unittest.TestCase):
    # In those tests you should enter Yandex value
    def test_market_test_nothing(self):
        self.assertEqual(main_parsing.market_choice(),
                         'https://market.yandex.ru/search?text=',
                         msg='testing for Yandex value')

    def test_market_numbers(self):
        self.assertEqual(main_parsing.market_choice(213),
                         'https://market.yandex.ru/search?text=')

    def test_market_yandex(self):
        self.assertEqual(main_parsing.market_choice('Yandex'),
                         'https://market.yandex.ru/search?text=',
                         msg='testing for Yandex value')

    def test_market_none(self):
        self.assertEqual(main_parsing.market_choice(None),
                         'https://market.yandex.ru/search?text=',
                         msg='testing for Yandex value')

    def test_market_zero(self):
        self.assertEqual(main_parsing.market_choice(0),
                         'https://market.yandex.ru/search?text=',
                         msg='testing for Yandex value')

    def test_market_one(self):
        self.assertEqual(main_parsing.market_choice('1'),
                         'https://market.yandex.ru/search?text=',
                         msg='testing for Yandex value')

    def test_market_two(self):
        self.assertEqual(main_parsing.market_choice('Ozon Yandex'),
                         'https://market.yandex.ru/search?text=',
                         msg='testing for Yandex value')


if __name__ == '__main__':
    unittest.main()
