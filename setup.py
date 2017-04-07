#!/usr/bin/python2.7

from setuptools import setup

setup(
    name='youtube-streamer',
    version='1.0.1',
    description='Stream youtube videos',
    long_description='This python package streams youtube videos based on user\'s query.',
    author='Dushyant Rathore',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stablegit
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords="Youtube video streamer",
    author_email='dushyant.bgs@gmail.com',
    url='https://github.com/dushyantRathore/Youtube-Streamer',
    packages=["ys"],
    scripts=["bin/ys"],
    install_requires=[
        "requests<=2.11.1",
        "beautifulsoup4",
        "prettytable"
    ]
)
