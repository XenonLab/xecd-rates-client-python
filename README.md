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

The preferred way to install this package is through Github.

```
pip install git+https://github.com/XenonLab/xecd-rates-client-python.git#egg=xecd_rates_client
```

Or you can clone the git repository :

```
git clone git@github.com:XenonLab/xecd-rates-client-python.git
```

And install the xecd client with build target :

```
cd xecd-rates-client-python && make build
```

Or install the xecd client with pip :

```
cd xecd-rates-client-python && pip install .
```

This package follows [semantic versioning][3].

## Usage

```python
from xecd_rates_client import XecdClient

xecd = XecdClient('accountId', 'apiKey')


response = xecd.account_info()
#do stuff with response
response = xecd.currencies()
response = xecd.convert_from("EUR", "CAD", 55)
response = xecd.convert_to("RUB", "CAD", 55)
response = xecd.historic_rate("2016-12-25", "12:34", "EUR", "CAD", 55)
response = xecd.historic_rate_period(55, "EUR", "RUB", "2016-02-28T12:00", "2016-03-03T12:00")
response = xecd.monthly_average(55, "CAD", "EUR", 2017, 5)
```

## Documentation

[Technical Specifications][2]

## Contributing

xecd_rates_client_python is an open-source project. Submit a pull request to contribute!

## Testing
You can use the build target that will launch unit and integration tests :

```bash
make test
```
Or use call python test modules from cmdline 

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