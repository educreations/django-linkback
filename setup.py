#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="django-rawid-linkback",
    version="0.1-ec1-70860fd",
    author='Lincoln Loop: Nicolas Lara',
    author_email='info@lincolnloop.com',
    description=("An admin widget to show a link back to the original objects in foreign keys."),
    packages=find_packages(),
    package_data={'linkback': [
        'static/linkback/js/*.js',
        'static/linkback/img/*.gif',
        'templates/linkback/*.html',
        'templates/linkback/admin/*.html',
        'templates/linkback/admin/widgets/*.html'
    ]},
    url="http://github.com/frewsxcv/django-linkback/",
    install_requires=['setuptools'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
