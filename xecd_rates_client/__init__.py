# -*- coding: utf-8 -*-
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
        Account info will return basic information for a specific account

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
        Currencies endpoint will return a list of all currencies, active \
        and obsolete, available via the XE Currency Data API.

        If the obsolete optional parameter is included, then the list will \
        contain both active and obsolete currencies.

        :param obsolete: ``OPTIONAL`` – If true then endpoint will display \
        currencies that are obsolete but for which historical data is \
        available
        :param language: ``OPTIONAL`` – parameter used to specify the language in \
        which you would like the currency names to be provided. Specified as \
        an RFC-1766-compliant language tag. \
        Currently supported languages include "ar", "de", "en", "es", "fr", \
        "it", "ja", "pt", "sv", "zh-CN" and "zh-HK". \
        If not specified, “en” is used.
        :param iso: ``OPTIONAL`` – Comma separated list of ISO 4217 codes. This \
        will limit the data returned to only those currencies that are \
        specified. \
        If this parameter is omitted, this endpoint will return results for \
        all currencies. \
        It is a prefix match; you can provide it with one, two, or three \
        characters and it will return a list of all the currencies with \
        **ISO 4217** codes that match. \
        A list of acceptable ISO 4217 currency codes can be found here: \
        http://www.xe.com/iso4217.php
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
        Convert from a currency amount to multiple other currencies using the \
        exchange rates appropriate to your purchased level of service \
        (Daily or Live).

        For example, if you have $110.23 USD, how much CAD \
        will that get you.

        :param fromCurrency: ``OPTIONAL`` - Currency you want to convert from ISO \
        code. Note if this parameter is omitted, USD is assumed.
        :param toCurrency: Comma separated list of to currencies ISO 4217 \
        codes. This will limit the data returned to only those currencies \
        that are specified. Use an asterisk * to convert all currencies. \
        Note: Obsolete currencies are replaced by their successor currency.
        :param amount: ``OPTIONAL`` – This parameter can be used to specify the \
        amount you want to convert, if an amount is not specified then 1 is \
        assumed.
        :param obsolete: ``OPTIONAL`` – If ‘true’ then endpoint will display rates\
        for currencies that are obsolete. If ‘false’ then obsolete currencies\
        are replaced by their successor currency.
        :param inverse: If ‘true’ then endpoint will include inverse rates. An\
        inverse rate is a quote for which the base currency and counter \
        currency are switched. An inverse is calculated by dividing one by \
        the exchange rate. \
        Example: If the exchange rate for $1 USD to EUR = 0.874852, then the \
        inverse rate would be 1/0.874852 = 1.14305, meaning that US$1.14305 \
        would buy 1 euro.
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
        Convert to a currency amount from multiple other currencies using the \
        exchange rates appropriate to your purchased level of service \
        (Daily or Live).

        For example, how much USD and EUR do you need to get $1000 CAD

        :param toCurrency: ``OPTIONAL`` - Currency you want to convert to ISO \
        code. \
        Note if thi sparameter is omitted, USD is assumed.
        :param fromCurrency: Comma separated list of to currencies ISO codes. \
         This will limit the data returned to only those currencies that are \
         specified. Use an asterisk * to convert all currencies. \
         Note: Obsolete currencies are replaced by their successor currency.
        :param amount: r ``OPTIONAL`` – This parameter can be used to specify the \
         amount you want to convert, if an amount is not specified then 1 is \
         assumed.
        :param obsolete: ``OPTIONAL`` – If ‘true’ then endpoint will display rates\
         for currencies that are obsolete. If ‘false’ then obsolete currencies\
          are replaced by their successor currency.
        :param inverse: ``OPTIONAL`` – If ‘true’ then endpoint will include \
        inverse rates.
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
        Returns the historic rate for a single base currency and one or more \
        counter currencies.

        :param date: UTC date should be in the form of YYYY-MM-DD, up to \
        1995-11-16. If your account is registered for a Daily package your \
        endpoint will return rates at your preferred daily lock-in time. \
        If your account is registered for a Live package your endpoint will \
        return XE mid-day rate unless you specify a time parameter in your \
        rate request.
        :param time: ``OPTIONAL`` – Time parameter is applicable to Live package \
        only – UTC time is in format of HH:MM \
        Time option is only available for the last 24 hours, if time is not \
        specified, only one table is returned using the XE mid-day rates \
        (As returned in http://www.xe.com/currencytables/)
        :param fromCurrency: ``OPTIONAL`` - Currency you want to convert from ISO \
        code. Note if this parameter is omitted, USD is assumed.
        :param toCurrency:  Comma separated list of to currencies ISO 4217 \
        codes. This will limit the data returned to only those currencies \
        that are specified. Use an asterisk * to specify all currencies. \
        Note: Obsolete currencies are replaced by their precursor or \
        successor currency
        :param amount: ``OPTIONAL`` – This parameter can be used to specify the \
        amount you want to convert, if an amount is not specified then 1 is \
        assumed
        :param obsolete: ``OPTIONAL`` – If ‘true’ then endpoint will display \
        rates for currencies that are obsolete. If ‘false’ then obsolete \
        currencies are replaced by their successor currency.
        :param inverse: ``OPTIONAL`` – If ‘true’ then endpoint will include \
        inverse rates.
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
        Returns a daily historic rate for a single base currency and one or \
        more counter currencies over a period of time.

        :param amount: ``OPTIONAL`` – This parameter can be used to specify \
        the amount you want to convert, if an amount is not specified then 1 \
        is assumed.
        :param fromCurrency: ``OPTIONAL`` - Currency you want to convert from \
        ISO code. Note if this parameter is omitted, USD is assumed.
        :param toCurrency: The target currency to calculate at rate for this \
        time period
        :param start_timestamp: ``OPTIONAL`` – ISO 8601 timestamp in the \
        format *yyyy-mm-ddThh:mm* giving the UTC date and time of the start \
         of the period for which you would like rates returned.\
        If your account is registered for a Daily package your endpoint will \
        return rates at your preferred daily lock-in time starting on the \
        date specified in your request. If your account does not have a \
        preferred daily lock-in time then rates will return as of 00:00 UTC.\
        If your account is registered for a Live package your endpoint will \
        return rates starting at 00:00 UTC if no time portion is specified.
        :param end_timestamp: ``OPTIONAL`` – ISO 8601 timestamp in the format \
        *yyyy-mm-ddThh:mm* giving the UTC date and time of the end of the \
        period for which you would like rates returned. If a time in the \
        future is specified, the current time will be used. \
        If no end_time is specified, the time specified in the \
        “start_timestamp” paramenter will also be used for the \
        end_timestamp.” \
        If your account is registered for a Daily package your endpoint will \
        return rates at your preferred daily lock-in time ending on the date \
        specified in your request. If your account does not have a preferred \
        daily lock-in time then rates will return as of 00:00 UTC. \
        If your account is registered for a Live package your endpoint will \
        return rates at 00:00 UTC unless you specify a time parameter in your \
        rate request.
        :param interval: ``OPTIONAL`` – Interval is applicable to Live \
        packages only. Using one of the interval values below in your rate \
        request will return rates for that specific interval within the \
        time period specified. \
        Example: adding the interval of “hourly” will return rates for every \
        hour in the time period you specified
        :param obsolete: ``OPTIONAL`` – If ‘true’ then endpoint will display \
        rates for currencies that are obsolete. If ‘false’ then obsolete \
        currencies are replaced by their successor currency.
        :param inverse: ``OPTIONAL`` – If ‘true’ then endpoint will include \
        inverse rates.
        :param page: ``OPTIONAL`` – This parameter can be used to specify the \
        number of decimal places included in the output. \
        Example 1 USD to EUR = 0.874852 with decimal_places=3, the output \
        returned will be EUR = 0.875
        :param per_page: ``OPTIONAL`` – You can specify the number of results \
        per page. The default is 30 results per page with a maximum of 100 \
        results per page.
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
        Returns monthly average rates for a single base currency and one or \
        more counter currencies for a year and optionally month. The monthly \
        average is calculated by taking the 00:00 UTC rate for each day in \
        the month/year you specify in your query.

        :param amount: ``OPTIONAL`` – This parameter can be used to specify the \
        amount you want to convert, if an amount is not specified then 1 \
        is assumed.
        :param fromCurrency: ``OPTIONAL`` - Currency you want to convert from ISO \
        code. Note if this parameter is omitted, USD is assumed.
        :param toCurrency: Comma separated list of to currencies based on ISO \
        4217 codes. This will limit the data returned to only those \
        currencies that are specified.
        :param year: ``OPTIONAL`` – This parameter specifies the year to \
        calculate average monthly rates.
        :param month: ``OPTIONAL`` – This parameter specifies the month in the \
        given year to return average monthly rates. This is a numeric value \
        from 1 to 12 where 1 is for January and 12 is for December. \
        If no month is provided, then all months for the given year are \
        returned.
        :param obsolete: ``OPTIONAL`` – If ‘true’ then endpoint will display \
        rates for currencies that are obsolete. If ‘false’ then obsolete \
        currencies are replaced by their successor currency
        :param inverse: ``OPTIONAL`` – If ‘true’ then endpoint will include \
        inverse rates.
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


