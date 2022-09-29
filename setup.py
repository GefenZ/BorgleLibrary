from imghdr import tests
from setuptools import setup, find_packages

setup(
    name='borgle',
    packages=find_packages(include=['borgle']),
    version='0.3.2',
    description='python library for borgle game',
    author='Gefen Zadok and Yoav Shifman',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    url="https://test.pypi.org/legacy/"
)