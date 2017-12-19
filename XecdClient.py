import requests

class XecdClient(object):
    """XECD Python Client Class"""
    def __init__(self, accountId, apiKey, options = {}):
            #python3.5 can do a = {**b, **c}, but it's too new, will leave it out
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

    #call with send(**options)
    def send(self, ops):
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
        return self.send(ops)

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
        return self.send(ops)

            #from is a python keyword, should avoid using
    def convert_from(self, fromCurrency = "USD", toCurrency = "*" , amount = 1, obsolete = False, inverse = False, options = {}):
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

    def convert_to(self, toCurrency = "USD", fromCurrency = "*" , amount = 1, obsolete = False, inverse = False, options = {}):
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

    def historic_rate(self, date, time, fromCurrency = "USD" , toCurrency = "*", amount = 1, obsolete = False, inverse = False, options = {}):
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

    def historic_rate_period(self, amount = 1, fromCurrency = "USD", toCurrency = "*", start_timestamp = None, end_timestamp = None, interval = "DAILY", obsolete = False, inverse = False, page = 1, per_page = 30, options = {}):
        ops = {
            'url': self.options['baseUrl'] + self.historicRatePeriodRequestUri,
            'qs': {
                'from': fromCurrency,
                'to': toCurrency,
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
        return self.send(ops)

    def monthly_average(self, amount = 1, fromCurrency = "USD", toCurrency = "*", year = None, month = None, obsolete = False, inverse = False, options = {}):
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
