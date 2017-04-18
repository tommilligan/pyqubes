#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pyqubes',
    version='0.0.1',
    license='Apache License 2.0',
    url='https://github.com/tommilligan/pyqubes/',
    author='Tom Milligan',
    author_email='code@tommilligan.net',
    description="Backend for synaptic-scout; request data from Neo4j, perform searches in Elastic, and pump data between the two.",
    keywords='neo neo4j elastic elasticsearch graph iterative',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: Apache Software License',
    ],
    zip_safe=False,
    platforms='any',
    install_requires=[
    ],
    tests_require=['nose2 >= 0.6.5'],
    test_suite='nose2.collector.collector',
    # Install these with "pip install -e isoprene_pumpjack[dev]
    extras_require={
        'dev': [
            'sphinx >= 1.5.3',
            'sphinx-argparse >= 0.1.17',
            'sphinx_rtd_theme >= 0.1.9',
            'codeclimate-test-reporter >= 0.2.1',
            'cov-core >= 1.15.0',
            'nose2 >= 0.6.5',
        ]
    },
    entry_points={
        'console_scripts': [
            'pyqubes = isoprene_pumpjack.api:main'
        ]
    },
)
