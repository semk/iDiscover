# -*- coding: utf-8 -*-

import os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


def readme(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='idiscover',
    version='1.0',
    description='Discover the devices (IP address & Manufacturer information) in a (sub)network',
    long_description=readme('README.md'),
    license='MIT License',
    keywords='Discover IP Address Manufacturer OUI ARP MAC',
    author='Sreejith Kesavan',
    author_email='sreejithemk@gmail.com',
    url='https://github.com/semk/iDiscover',
    download_url='https://github.com/semk/iDiscover/tarball/master',
    install_requires=['ipcalc >= 1.1.2'],
    packages=find_packages(),
    package_data={
        'idiscover': ['data/*.txt'],
    },
    include_package_data=True,
    entry_points={
        'console_scripts': ['idiscover = idiscover.discover:run']
    },
    platforms=['any'],
    classifiers=[
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Environment :: Console',
        'Topic :: System :: Networking',
        'Topic :: Utilities'
    ],
    zip_safe=True
)