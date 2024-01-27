import unittest
from unittest.mock import patch
from bitcoin_price_index import get_bitcoin_price, calculate_total

class TestBitcoinPriceIndex(unittest.TestCase):

    @patch('bitcoin_price_index.requests.get')
    def test_get_bitcoin_price_success(self, mock_requests):
        mock_response = mock_requests.return_value
        mock_response.json.return_value = {'bpi': {'USD': {'rate': '50000'}}}
        bitcoin_price = get_bitcoin_price()
        self.assertEqual(bitcoin_price, 50000.0)

    @patch('bitcoin_price_index.requests.get', side_effect=requests.RequestException)
    def test_get_bitcoin_price_failure(self, mock_requests):
        bitcoin_price = get_bitcoin_price()
        self.assertIsNone(bitcoin_price)

    def test_calculate_total(self):
        bitcoin_price = 50000.0
        amount_of_bitcoin = 0.5
        total = calculate_total(bitcoin_price, amount_of_bitcoin)
        self.assertEqual(total, 25000.0)

    def test_calculate_total_zero_bitcoin(self):
        bitcoin_price = 50000.0
        amount_of_bitcoin = 0.0
        total = calculate_total(bitcoin_price, amount_of_bitcoin)
        self.assertEqual(total, 0.0)

    def test_calculate_total_negative_bitcoin(self):
        bitcoin_price = 50000.0
        amount_of_bitcoin = -0.5
        total = calculate_total(bitcoin_price, amount_of_bitcoin)
        self.assertEqual(total, -25000.0)

if __name__ == '__main__':
    unittest.main()
