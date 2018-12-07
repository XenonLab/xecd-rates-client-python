from xecd_rates_client import XecdClient
import unittest
import os


class XecdClientIntegrationTest(unittest.TestCase):

    def setUp(self):
        self.xecd = XecdClient(os.environ['XecdAccountID'], os.environ['XecdApiKey'])

    def testAccountInfo(self):
        response = self.xecd.account_info()
        self.assertIn('id', response)
        self.assertIn('organization', response)
        self.assertIn('package', response)
        self.assertIn('service_start_timestamp', response)
        
    def testCurrencies(self):
        response = self.xecd.currencies()
        self.assertIn('terms', response)
        self.assertIn('privacy', response)
        self.assertIn('currencies', response)

    def testConvertFrom(self):
        response = self.xecd.convert_from("EUR", "CAD", 55)
        self.assertIn('terms', response)
        self.assertIn('privacy', response)
        self.assertIn('from', response)
        self.assertIn('amount', response)
        self.assertIn('timestamp', response)
        self.assertIn('to', response)

    def testConvertTo(self):
        response = self.xecd.convert_to("RUB", "CAD", 55)
        self.assertIn('terms', response)
        self.assertIn('privacy', response)
        self.assertIn('to', response)
        self.assertIn('amount', response)
        self.assertIn('timestamp', response)
        self.assertIn('from', response)

    def testHistoricRate(self):
        response = self.xecd.historic_rate("2016-12-25", "12:34", "EUR", "CAD", 55)
        self.assertIn('terms', response)
        self.assertIn('privacy', response)
        self.assertIn('from', response)
        self.assertIn('amount', response)
        self.assertIn('timestamp', response)
        self.assertIn('to', response)

    def testHistoricRatePeriod(self):
        response = self.xecd.historic_rate_period(55, "EUR", "RUB", "2017-09-28T12:00", "2017-10-03T12:00")
        self.assertIn('terms', response)
        self.assertIn('privacy', response)
        self.assertIn('from', response)
        self.assertIn('amount', response)
        self.assertIn('to', response)

    def testMonthlyAverage(self):
        response = self.xecd.monthly_average(55, "CAD", "EUR", 2017, 5)
        self.assertIn('terms', response)
        self.assertIn('privacy', response)
        self.assertIn('from', response)
        self.assertIn('amount', response)
        self.assertIn('year', response)
        self.assertIn('to', response)
