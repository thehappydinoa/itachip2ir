from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='itachip2ir',
    version='1.3.2',
    description='A small Python module for interacting with the Global Cache iTach WF2IR or IP2IR',
    long_description=long_description,
    url='https://github.com/thehappydinoa/itachip2ir',
    author='Aidan Holland (thehappydinoa)',
    author_email='thehappydinoa@gmail.com',

    classifiers=[
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],

    keywords='itach ip2ir Global Cache ir smart-home',

    packages=find_packages(exclude=['contrib', 'docs', 'tests', "examples"]),

    project_urls={
        'Bug Reports': 'https://github.com/thehappydinoa/itachip2ir/issues',
        'Say Thanks!': 'http://saythanks.io/to/thehappydinoa',
        'Contribute!': 'https://github.com/thehappydinoa/itachip2ir/pulls',
        'Follow Me!': 'https://twitter.com/thehappydinoa/'
    },
)
