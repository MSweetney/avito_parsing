import unittest
from avito_parser import main_parsing

# THOSE TESTS ARE OLD IGNORE THEM
# THOSE TESTS ARE OLD IGNORE THEM
# THOSE TESTS ARE OLD IGNORE THEM


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
