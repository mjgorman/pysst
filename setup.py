#!/usr/bin/env python3

from setuptools import setup, find_packages

long_description = """
Pyyst is a system security scanning framework.

Using behave to setup a BDD style scenario collection allowing
for anyone in the org to to write new scenarios.
"""

setup(
    name='pysst',
    version="0.0.1",
    description='Python System Security Testing',
    long_description=long_description,
    author='Michael J. Gorman',
    author_email='michael@michaeljgorman.com',
    url='https://github.com/mjgorman/pysst',
    packages=find_packages(),
    package_data={'': ['skeleton/example.feature',
                       'skeleton/steps/example.py']
                 },
    include_package_data=True,
    entry_points = {
              'console_scripts': [
                  'pysst = pysst.main:main',
              ],
          },
    install_requires=['behave==1.2.6',
                      'python-nmap==0.6.1',
                      'requests==2.21.0',
                     ],
    tests_require=['pytest==4.4.1', 'pytest-cov'],
    setup_requires=['pytest-runner', 'pytest-cov']
)
