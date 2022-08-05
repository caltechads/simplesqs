from setuptools import setup, find_packages

setup(
    name='simplesqs',
    version="0.2.1",
    description='A library for sending and receiving AWS SQS messages.',
    long_description=open('README.rst', 'rt').read(),
    author="IMSS ADS",
    author_email="imss-ads-staff@caltech.edu",
    url='https://bitbucket.org/caltech-imss-ads/simplesqs',
    packages=find_packages(exclude=['bin']),
    include_package_data=True,
)
