<p align="">
    <a href="http://www.xe.com" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/en/5/55/XE_Corporation_logo.png" width="90" height="72"/>
    </a>
</p>

# XE Currency Data Client - Python

XE.com Inc. is the World's Trusted Currency Authority. This project provides an SDK to interface with our XE Currency Data (XECD) product.

XE Currency Data is a REST API that gives you access to daily or live rates and historic mid-market conversion rates between all of our supported currencies.

You will need an api key and secret to use this sdk. Sign up for a [free trial][4] or register for a [full account][5].

This client will work with both python2 and python3.

## Installation

The preferred way to install this package is pip.

```
pip install xecd-rates-client
```

Or get the latest version from git:
```
pip install git+https://github.com/XenonLab/xecd-rates-client-python.git
```


This package follows [semantic versioning][3].

## Usage

```python
>>> from xecd_rates_client import XecdClient
>>> xecd = XecdClient('ACCOUNT_ID', 'API_KEY')

>>> xecd.account_info()
{'id': '11111111-1111-1111-1111-111111111111', 'organization': 'YOUR_ORG', 'package': 'ENTERPRISE_LIVE_INTERNAL', 'service_start_timestamp': '2018-01-01T00:00:00Z'}

>>> xecd.convert_from("EUR", "CAD", 55)
{'terms': 'http://www.xe.com/legal/dfs.php', 'privacy': 'http://www.xe.com/privacy.php', 'from': 'EUR', 'amount': 55.0, 'timestamp': '2018-08-21T15:31:00Z', 'to': [{'quotecurrency': 'CAD', 'mid': 82.7121317322}]}

>>> xecd.convert_to("RUB", "CAD", 55)
{'terms': 'http://www.xe.com/legal/dfs.php', 'privacy': 'http://www.xe.com/privacy.php', 'to': 'RUB', 'amount': 55.0, 'timestamp': '2018-08-21T15:32:00Z', 'from': [{'quotecurrency': 'CAD', 'mid': 1.0652293852}]}

>>> xecd.historic_rate("2016-12-25", "12:34", "EUR", "CAD", 55)
{'terms': 'http://www.xe.com/legal/dfs.php', 'privacy': 'http://www.xe.com/privacy.php', 'from': 'EUR', 'amount': 55.0, 'timestamp': '2016-12-25T13:00:00Z', 'to': [{'quotecurrency': 'CAD', 'mid': 77.8883951909}]}

>>> xecd.historic_rate_period(55, "EUR", "RUB", "2016-02-28T12:00", "2016-03-03T12:00")
{'terms': 'http://www.xe.com/legal/dfs.php', 'privacy': 'http://www.xe.com/privacy.php', 'from': 'EUR', 'amount': 55.0, 'to': {'RUB': [{'mid': 4590.1222691671, 'timestamp': '2016-02-28T12:00:00Z'}, {'mid': 4545.42879069, 'timestamp': '2016-02-29T12:00:00Z'}, {'mid': 4433.0643335184, 'timestamp': '2016-03-01T12:00:00Z'}, {'mid': 4409.6291908683, 'timestamp': '2016-03-02T12:00:00Z'}, {'mid': 4396.2068371801, 'timestamp': '2016-03-03T12:00:00Z'}]}}

>>> xecd.monthly_average(55, "CAD", "EUR", 2017, 5)
{'terms': 'http://www.xe.com/legal/dfs.php', 'privacy': 'http://www.xe.com/privacy.php', 'from': 'CAD', 'amount': 55.0, 'year': 2017, 'to': {'EUR': [{'monthlyAverage': 36.5976590134, 'month': 5, 'daysInMonth': 31}]}}
```

## Documentation

[Technical Specifications][2]

## Contributing

xecd_rates_client_python is an open-source project. Submit a pull request to contribute!

## Testing

```bash
python3 -m test.UnitTest
python3 -m test.IntegrationTest
python -m test.IntegrationTest
```

Note: the UnitTest must be ran with python3 due to its use of unittest.mock (which is not present as of python2.7). Despite this, the client itself is usable with both python 2 and 3.

## Security Issues

If you discover a security vulnerability within this package, please **DO NOT** publish it publicly. Instead, contact us at **security [at] xe.com**. We will follow up with you as soon as possible.

## About Us

[XE.com Inc.][1] is The World's Trusted Currency Authority. Development of this project is led by the XE.com Inc. Development Team and supported by the open-source community.

[1]: http://www.xe.com
[2]: http://www.xe.com/xecurrencydata/XE_Currency_Data_API_Specifications.pdf
[3]: http://semver.org/
[4]: https://xecd.xe.com/account/signup.php?freetrial
[5]: http://www.xe.com/xecurrencydata/