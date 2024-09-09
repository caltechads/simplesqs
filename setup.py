import os
from setuptools import setup, find_packages

def get_long_description():
    """Get the long description from the README file."""
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name='simplesqs',
    version="0.4.0",
    description='A library for sending and receiving AWS SQS messages.',
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Glenn W. Bach",
    author_email="imss-ads-staff@caltech.edu",
    url='https://github.com/caltechads/simplesqs',
    license="MIT License",
    classifiers=[  # Optional
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Networking',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    packages=find_packages(exclude=['bin']),
    include_package_data=True,
    python_requires='>=3.7, <4',
    install_requires=['boto3'],  # For AWS SQS interactions
)
