#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pyqubes',
    version='0.0.3',
    license='Apache License 2.0',
    url='https://github.com/tommilligan/pyqubes/',
    author='Tom Milligan',
    author_email='code@tommilligan.net',
    description="QubesOS dom0 automation in Python",
    keywords='qubes qubesos QubesOS wrapper recipe dom0 vm templatevm appvm',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Topic :: Desktop Environment',
        'Topic :: System :: Installation/Setup'
    ],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'six >= 1.10.0'
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
            'mock >= 2.0.0'
        ]
    },
    entry_points={
        'console_scripts': [
        ]
    },
)
