from setuptools import setup, find_packages

def readme():
    with open('README.rst') as f:
        return f.read()


doc_requires = ['sphinx', 'numpydoc', 'sphinx-rtd-theme']
test_requires = ['coverage', 'pytest == 3.3.1', 'pytest-mock']
install_requires = ['requests']

dev_requires = doc_requires + test_requires
complete_requires = dev_requires + test_requires + doc_requires

extra_requires = {
    'docs': doc_requires,
    'test': test_requires,
    'dev': dev_requires,
    'complete': complete_requires,
}
setup(
    name='xecd_rates_client',
    version='0.1.0',
    description='XECD REST Client',
    license='MPL-2.0',
    author='XE.com Inc. Development Team',
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    url='https://github.com/XenonLab/xecd-rates-client-python',
    packages=['xecd_rates_client'],
    include_package_data=True,
    install_requires=install_requires,
    extras_require=extra_requires,
    zip_safe=False
)
