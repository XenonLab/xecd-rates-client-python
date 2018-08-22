import requests

class XecdClient(object):
    """XECD REST API Client"""

    def __init__(self, account_id, api_key, options = {}):
        self.options = {
            'auth': {
                'user': account_id,
                'password': api_key
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

    def __send(self, ops):
        self.options.update(ops)
        #cached for debugging purposes
        url = self.options["url"]
        username = self.options['auth']['user']
        password = self.options['auth']['password']
        qs = self.options['qs']
        temp = requests.get(url, auth=(username, password), params=qs)
        data = temp.json()
        return data

    def account_info(self, options = {}):
        ops = {
            'url': self.options['baseUrl'] + self.accountInfoRequestUri
        }
        ops.update(options)
        return self.__send(ops)

    def currencies(self, obsolete = False, language = "en", iso = ['*'], options = {}):
        ops = {
            'url': self.options['baseUrl'] + self.currenciesRequestUri,
            'qs': {
                'obsolete': True if obsolete else False,
                'language': language,
                'iso': ','.join(iso) #format: abc,def,ghi
            }
        }
        ops.update(options)
        return self.__send(ops)

    def convert_from(self, from_currency ="USD", to_currency ="*", amount = 1, obsolete = False, inverse = False, options = {}):
        ops = {
            'url': self.options['baseUrl'] + self.convertFromRequestUri,
            'qs': {
                'from': from_currency,
                'to': to_currency,
                'amount': amount,
                'obsolete': True if obsolete else False,
                'inverse': True if inverse else False
            }
        }
        ops.update(options)
        return self.__send(ops)

    def convert_to(self, to_currency ="USD", from_currency ="*", amount = 1, obsolete = False, inverse = False, options = {}):
        ops = {
            'url': self.options['baseUrl'] + self.convertToRequestUri,
            'qs': {
                'to': to_currency,
                'from': from_currency,
                'amount': amount,
                'obsolete': True if obsolete else False,
                'inverse': True if inverse else False
            }
        }
        ops.update(options)
        return self.__send(ops)

    def historic_rate(self, date, time, from_currency ="USD", to_currency ="*", amount = 1, obsolete = False, inverse = False, options = {}):
        ops = {
            'url': self.options['baseUrl'] + self.historicRateRequestUri,
            'qs': {
                'from': from_currency,
                'to': to_currency,
                'amount': amount,
                'date': date,
                'time': time,
                'obsolete': True if obsolete else False,
                'inverse': True if inverse else False
            }
        }
        ops.update(options)
        return self.__send(ops)

    def historic_rate_period(self, amount = 1, from_currency ="USD", to_currency ="*", start_timestamp = None, end_timestamp = None, interval ="DAILY", obsolete = False, inverse = False, page = 1, per_page = 30, options = {}):
        ops = {
            'url': self.options['baseUrl'] + self.historicRatePeriodRequestUri,
            'qs': {
                'from': from_currency,
                'to': to_currency,
                'amount': amount,
                'start_timestamp': start_timestamp if (start_timestamp != None) else None,
                'end_timestamp': end_timestamp if (end_timestamp != None) else None,
                'interval': interval,
                'obsolete': True if obsolete else False,
                'inverse': True if inverse else False,
                'page': page,
                'per_page': per_page

            }
        }
        ops.update(options)
        return self.__send(ops)

    def monthly_average(self, amount = 1, from_currency ="USD", to_currency ="*", year = None, month = None, obsolete = False, inverse = False, options = {}):
        ops = {
            'url': self.options['baseUrl'] + self.monthlyAverageRequestUri,
            'qs': {
                'from': from_currency,
                'to': to_currency,
                'amount': amount,
                'year': year,
                'month': month,
                'obsolete': True if obsolete else False,
                'inverse': True if inverse else False
            }
        }
        ops.update(options)
        return self.__send(ops)
