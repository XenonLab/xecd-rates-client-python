from xecd_rates_client import XecdClient
import unittest
from unittest import mock
import json
import copy
with open('tests/data/testdata.json') as json_data:
    data = json.load(json_data)


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = copy.deepcopy(json_data)
        self.status_code = status_code

    def json(self):
        return self.json_data


class XecdClientUnitTest(unittest.TestCase):

    def setUp(self):
        self.xecd = XecdClient('accountId', 'apiKey')

    @mock.patch('requests.get', return_value=MockResponse(data["fakeAccountInfo"], 200))
    def testAccountInfo(self, mock_get):
        self.assertEqual(data["fakeAccountInfo"], self.xecd.account_info())

    @mock.patch('requests.get', return_value=MockResponse(data["fakeCurrencies"], 200))
    def testCurrencies(self, mock_get):
        self.assertEqual(data["fakeCurrencies"], self.xecd.currencies())

    @mock.patch('requests.get', return_value=MockResponse(data["fakeConvertFrom"], 200))
    def testConvertFrom(self, mock_get):
        self.assertEqual(data["fakeConvertFrom"], self.xecd.convert_from("EUR", "CAD", 55))

    @mock.patch('requests.get', return_value=MockResponse(data["fakeConvertTo"], 200))
    def testConvertTo(self, mock_get):
        self.assertEqual(data["fakeConvertTo"], self.xecd.convert_to("RUB", "CAD", 55))

    @mock.patch('requests.get', return_value=MockResponse(data["fakeHistoricRate"], 200))
    def testHistoricRate(self, mock_get):
        self.assertEqual(data["fakeHistoricRate"], self.xecd.historic_rate("2016-12-25", "12:34", "EUR", "CAD", 55))

    @mock.patch('requests.get', return_value=MockResponse(data["fakeHistoricRatePeriod"], 200))
    def testHistoricRatePeriod(self, mock_get):
        self.assertEqual(data["fakeHistoricRatePeriod"], self.xecd.historic_rate_period(55, "EUR", "RUB", "2016-02-28T12:00", "2016-03-03T12:00"))

    @mock.patch('requests.get', return_value=MockResponse(data["fakeMonthlyAverage"], 200))
    def testMonthlyAverage(self, mock_get):
        self.assertEqual(data["fakeMonthlyAverage"], self.xecd.monthly_average(55, "CAD", "EUR", 2017, 5))
