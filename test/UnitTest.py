"""
These tests will mock the responses of the api
Purposes of these tests is to see the functions are handling the returned data properly
These tests must be ran with python3 FROM parent directory
Sample:
    python3 -m test.UnitTest
"""
from XecdClient import XecdClient
import unittest
from unittest import mock
import json
with open('test/data/testdata.json') as json_data:
    data = json.load(json_data)


print("Running Unit Tests...")
xecd = XecdClient('accountId', 'apiKey')


"""mocking class"""
def mockingResponse(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if args[0] == xecd.options['baseUrl'] + xecd.accountInfoRequestUri:
        return MockResponse(data["fakeAccountInfo"], 200)
    elif args[0] == xecd.options['baseUrl'] + xecd.currenciesRequestUri:
        return MockResponse(data["fakeCurrencies"], 200)
    elif args[0] == xecd.options['baseUrl'] + xecd.convertFromRequestUri:
        return MockResponse(data["fakeConvertFrom"], 200)
    elif args[0] == xecd.options['baseUrl'] + xecd.convertToRequestUri:
        return MockResponse(data["fakeConvertTo"], 200)
    elif args[0] == xecd.options['baseUrl'] + xecd.historicRateRequestUri:
        return MockResponse(data["fakeHistoricRate"], 200)
    elif args[0] == xecd.options['baseUrl'] + xecd.historicRatePeriodRequestUri:
        return MockResponse(data["fakeHistoricRatePeriod"], 200)
    elif args[0] == xecd.options['baseUrl'] + xecd.monthlyAverageRequestUri:
        return MockResponse(data["fakeMonthlyAverage"], 200)
    return MockResponse(None, 404)



"""patch the class' request.get with the fake one"""
@mock.patch('XecdClient.requests.get', side_effect = mockingResponse)
    #has to be out here because it unpatches at the end of any testCASE

class unitTest(unittest.TestCase):
    def testAccountInfo(self, mock_get):
        response = xecd.account_info()
        differenceSet = set(response) ^ set(data["fakeAccountInfo"])
        assert len(differenceSet) == 0
            #Python does not have native javascript objects, things are dictionaries
            #Request.get returns extra information encoded into the returned string, gone after python parses it
            #Dictionaries are unordered, simple comparison does not work well
            #Using XOR to check set differences is more efficient than coding my own loop with comparisons
    
    def testCurrencies(self, mock_get):
        response = xecd.currencies()
        differenceSet = set(response) ^ set(data["fakeCurrencies"])
        assert len(differenceSet) == 0

    def testConvertFrom(self, mock_get):
        response = xecd.convert_from("EUR", "CAD", 55)
        differenceSet = set(response) ^ set(data["fakeConvertFrom"])
        assert len(differenceSet) == 0

    def testConvertTo(self, mock_get):
        response = xecd.convert_to("RUB", "CAD", 55)
        differenceSet = set(response) ^ set(data["fakeConvertTo"])
        assert len(differenceSet) == 0

    def testHistoricRate(self, mock_get):
        response = xecd.historic_rate("2016-12-25", "12:34", "EUR", "CAD", 55)
        differenceSet = set(response) ^ set(data["fakeHistoricRate"])
        assert len(differenceSet) == 0

    def testHistoricRatePeriod(self, mock_get):
        response = xecd.historic_rate_period(55, "EUR", "RUB", "2016-02-28T12:00", "2016-03-03T12:00")
        differenceSet = set(response) ^ set(data["fakeHistoricRatePeriod"])
        assert len(differenceSet) == 0

    def testMonthlyAverage(self, mock_get):
        response = xecd.monthly_average(55, "CAD", "EUR", 2017, 5)
        differenceSet = set(response) ^ set(data["fakeMonthlyAverage"])
        assert len(differenceSet) == 0


unittest.main() #this actually runs the tests
