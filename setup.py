# coding: utf-8
from distutils.core import setup

setup(
    name='django-shuffler',
    version='0.01',
    description='Mixing DB data for faking personal data.',
    author='Telminov Sergey',
    url='https://github.com/telminov/shuffler',
    packages=['shuffler',],
    long_description=open('README.md').read(),
    license='The MIT License',
)
