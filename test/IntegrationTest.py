"""
The accountId and apiKey will be in environment variables so they remain secure.
Can also be executed with string/var input parameters:
    xecd = XecdClient('accountId', apiKeyStrVar)

Can be ran in any python version FROM parent directory
Samples:
    (source /path/xecdVars) - unneccessary if running with strings, or if set into env file
    python3 -m test.IntegrationTest
    python -m test.IntegrationTest
"""
from XecdClient import XecdClient
import unittest
import json
import os #not needed if not using environment variables

print("Running Integration Tests...")
xecd = XecdClient(os.environ['XecdAccountID'], os.environ['XecdApiKey'])

class requestResponseTest(unittest.TestCase):
    def testAccountInfo(self):
        response = xecd.account_info()
        jsonData = json.dumps(response)
        assert jsonData is not None
        assert 'id' in jsonData
        assert 'organization' in jsonData
        assert 'package' in jsonData
        assert 'service_start_timestamp' in jsonData
        
    def testCurrencies(self):
        response = xecd.currencies()
        jsonData = json.dumps(response)
        assert jsonData is not None
        assert 'terms' in jsonData
        assert 'privacy' in jsonData
        assert 'currencies' in jsonData

    def testConvertFrom(self):
        response = xecd.convert_from("EUR", "CAD", 55)
        jsonData = json.dumps(response)
        assert jsonData is not None
        assert 'terms' in jsonData
        assert 'privacy' in jsonData
        assert 'from' in jsonData
        assert 'amount' in jsonData
        assert 'timestamp' in jsonData
        assert 'to' in jsonData

    def testConvertTo(self):
        response = xecd.convert_to("RUB", "CAD", 55)
        jsonData = json.dumps(response)
        assert jsonData is not None
        assert 'terms' in jsonData
        assert 'privacy' in jsonData
        assert 'to' in jsonData
        assert 'amount' in jsonData
        assert 'timestamp' in jsonData
        assert 'from' in jsonData

    def testHistoricRate(self):
        response = xecd.historic_rate("2016-12-25", "12:34", "EUR", "CAD", 55)
        jsonData = json.dumps(response)
        assert jsonData is not None
        assert 'terms' in jsonData
        assert 'privacy' in jsonData
        assert 'from' in jsonData
        assert 'amount' in jsonData
        assert 'timestamp' in jsonData
        assert 'to' in jsonData

    def testHistoricRatePeriod(self):
        response = xecd.historic_rate_period(55, "EUR", "RUB", "2017-09-28T12:00", "2017-10-03T12:00")
        jsonData = json.dumps(response)
        assert jsonData is not None
        assert 'terms' in jsonData
        assert 'privacy' in jsonData
        assert 'from' in jsonData
        assert 'amount' in jsonData
        assert 'to' in jsonData

    def testMonthlyAverage(self):
        response = xecd.monthly_average(55, "CAD", "EUR", 2017, 5)
        jsonData = json.dumps(response)
        assert jsonData is not None
        assert 'terms' in jsonData
        assert 'privacy' in jsonData
        assert 'from' in jsonData
        assert 'amount' in jsonData
        assert 'year' in jsonData
        assert 'to' in jsonData


unittest.main() #this actually runs the tests
