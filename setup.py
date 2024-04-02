from setuptools import setup, find_packages

setup(
    name='pi-avionics',
    version='0.1.0',
    description='Repository for code to run on the raspberry pi for avionics applications',
    author='Benedict Rose',
    author_email='brbenrose@gmail.com',
    packages=find_packages(),
    install_requires=[
        'picamera',
        'numpy',
    ],
)