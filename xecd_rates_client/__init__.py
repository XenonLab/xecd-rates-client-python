"""
Xecd Rest HTTP Client
~~~~~~~~~~~~~~~~~~~~~

XecdClient is an HTTP library, written in Python, for human beings. Basic GET

:usage:

>>> from xecd_rates_client import XecdClient
>>> xecd = XecdClient('accountId', 'apiKey')
>>> response = xecd.account_info()
>>> response = xecd.currencies()
>>> response = xecd.convert_from("EUR", "CAD", 55)
>>> response = xecd.convert_to("RUB", "CAD", 55)
>>> response = xecd.historic_rate("2016-12-25", "12:34", "EUR", "CAD", 55)
>>> response = xecd.historic_rate_period(55, "EUR", "RUB", "2016-02-28T12:00", "2016-03-03T12:00")
>>> response = xecd.monthly_average(55, "CAD", "EUR", 2017, 5)

:copyright: (c) 2018 by XE.com Inc. Development Team.
:license: MPL-2.0, see LICENSE for more details.
"""

import requests


class XecdClient(object):
    """XECD Python Client Class"""

    def __init__(self, accountId, apiKey, options={}):
        # python3.5 can do a = {**b, **c}, but it's too new, will leave it out
        self.options = {
            'auth': {
                'user': accountId,
                'password': apiKey
            },
            'baseUrl': 'https://xecdapi.xe.com/v1/',
            'qs': {}
        }
        self.options.update(options)

        self.accountInfoRequestUri = 'account_info.json'
        self.currenciesRequestUri = 'currencies.json'
        self.convertFromRequestUri = 'convert_from.json'
        self.convertToRequestUri = 'convert_to.json'
        self.historicRateRequestUri = 'historic_rate.json'
        self.historicRatePeriodRequestUri = 'historic_rate/period.json'
        self.monthlyAverageRequestUri = 'monthly_average.json'

    # call with send(**options)
    def send(self, ops):
        """
        The send method sends request to xe api

        :param ops: options to add for http client request
        :return: `data` json response object
        """
        self.options.update(ops)
        # cached for debugging purposes
        url = self.options["url"]
        username = self.options['auth']['user']
        password = self.options['auth']['password']
        qs = self.options['qs']
        temp = requests.get(url, auth=(username, password), params=qs)
        data = temp.json()
        return data

    def account_info(self, options={}):
        """
        This methods retrieves account info

        :param options: options to add for http client request
        :return: `data` json response object
        """
        ops = {
            'url': self.options['baseUrl'] + self.accountInfoRequestUri
        }
        ops.update(options)
        return self.send(ops)

    def currencies(self, obsolete=False, language="en", iso=['*'], options={}):
        """
        The currencies method retrieves the currently available currencies

        :param obsolete: The obsolete currencies
        :param language: The language to use
        :param iso: The iso code
        :param options: The options to add for http client request
        :return: `data` json response object
        """
        ops = {
            'url': self.options['baseUrl'] + self.currenciesRequestUri,
            'qs': {
                'obsolete': True if obsolete else False,
                'language': language,
                'iso': ','.join(iso)  # format: abc,def,ghi
            }
        }
        ops.update(options)
        return self.send(ops)

        # from is a python keyword, should avoid using

    def convert_from(self, fromCurrency="USD", toCurrency="*", amount=1,
                     obsolete=False, inverse=False, options={}):
        """
        The convert_from method converts a given currency to another for a
        given amount

        :param fromCurrency: The currency from which calculate the rate
        :param toCurrency: The target current to calculate at rate
        :param amount: The amount of fromCurrency to convert
        :param obsolete: The obsolete currencies
        :param inverse: Return response inverted
        :param options: Options to add for http client request
        :return: `data` json response object
        """
        ops = {
            'url': self.options['baseUrl'] + self.convertFromRequestUri,
            'qs': {
                'from': fromCurrency,
                'to': toCurrency,
                'amount': amount,
                'obsolete': True if obsolete else False,
                'inverse': True if inverse else False
            }
        }
        ops.update(options)
        return self.send(ops)

    def convert_to(self, toCurrency="USD", fromCurrency="*", amount=1,
                   obsolete=False, inverse=False, options={}):
        """
        The convert_to method converts a given currency to another for a
        given amount

        :param toCurrency: The currency to which calculate the rate
        :param fromCurrency: The target currency to calculate at rate
        :param amount: The amount of toCurrency to convert
        :param obsolete: The obsolete currencies
        :param inverse: Return response inverted
        :param options: Options to add for http client request
        :return: `data` json response object
        """
        ops = {
            'url': self.options['baseUrl'] + self.convertToRequestUri,
            'qs': {
                'to': toCurrency,
                'from': fromCurrency,
                'amount': amount,
                'obsolete': True if obsolete else False,
                'inverse': True if inverse else False
            }
        }
        ops.update(options)
        return self.send(ops)

    def historic_rate(self, date, time, fromCurrency="USD", toCurrency="*",
                      amount=1, obsolete=False, inverse=False, options={}):
        """
        The historic_rate method provides historic rates for a given currency

        :param date: The date to get rate for a currency
        :param time: The time to get rate for a currency
        :param fromCurrency: The currency from which calculate the rate
        :param toCurrency:  The target currency to calculate at rate at time
        :param amount: The amoutn of fromCurrency to convert
        :param obsolete: The obsolete currencies
        :param inverse: Return response inverted
        :param options: Options to add for http client request
        :return: `data` json response object
        """
        ops = {
            'url': self.options['baseUrl'] + self.historicRateRequestUri,
            'qs': {
                'from': fromCurrency,
                'to': toCurrency,
                'amount': amount,
                'date': date,
                'time': time,
                'obsolete': True if obsolete else False,
                'inverse': True if inverse else False
            }
        }
        ops.update(options)
        return self.send(ops)

    def historic_rate_period(self, amount=1, fromCurrency="USD",
                             toCurrency="*", start_timestamp=None,
                             end_timestamp=None, interval="DAILY",
                             obsolete=False, inverse=False, page=1,
                             per_page=30, options={}):
        """
        The historic_rate_period provides historic rate for a given currency
        and a given period

        :param amount: The amount of currency to calculate at rate for this \
        period.
        :param fromCurrency: The currency from which calculate the rate.
        :param toCurrency: The target currency to calculate at rate for this \
        time period
        :param start_timestamp: The start timestamp for the period
        :param end_timestamp: The end timestamp for the period
        :param interval: The interval to get rates during that period
        :param obsolete: The obsolete currencies
        :param inverse: Return response inverted
        :param page: Page number for pagination
        :param per_page: Number of results per page
        :param options: Options to add for http client request
        :return: `data` json response object
        """
        ops = {
            'url': self.options['baseUrl'] + self.historicRatePeriodRequestUri,
            'qs': {
                'from': fromCurrency,
                'to': toCurrency,
                'amount': amount,
                'start_timestamp': start_timestamp if (
                        start_timestamp != None) else None,
                'end_timestamp': end_timestamp if (
                        end_timestamp != None) else None,
                'interval': interval,
                'obsolete': True if obsolete else False,
                'inverse': True if inverse else False,
                'page': page,
                'per_page': per_page

            }
        }
        ops.update(options)
        return self.send(ops)

    def monthly_average(self, amount=1, fromCurrency="USD", toCurrency="*",
                        year=None, month=None, obsolete=False, inverse=False,
                        options={}):
        """
        The monthly_average method calculates monthly average for a given
        currency and a given period

        :param amount: The amount of currency to calculate at rate for this \
        period.
        :param fromCurrency: The currency from which calculate the rate.
        :param toCurrency:  The target currency to calculate at rate for this \
        time period
        :param year: The year to calculate the monthly average
        :param month: The month to calculate the monthly average
        :param obsolete: The obsolete currencies
        :param inverse: Return response inverted
        :param options: Options to add for http client request
        :return: `data` json response object
        """
        ops = {
            'url': self.options['baseUrl'] + self.monthlyAverageRequestUri,
            'qs': {
                'from': fromCurrency,
                'to': toCurrency,
                'amount': amount,
                'year': year,
                'month': month,
                'obsolete': True if obsolete else False,
                'inverse': True if inverse else False
            }
        }
        ops.update(options)
        return self.send(ops)


