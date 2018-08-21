import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='xecd_rates_client',
    version='1.0.0',
    url='https://github.com/XenonLab/xecd-rates-client-python',
    packages=setuptools.find_packages(exclude=['test*']),
    description='XECD REST Client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='XE.com Inc. Development Team',
    author_email='python@xe.com',
    zip_safe=True,
    install_requires=[
        'requests>=2.19.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ]
)
