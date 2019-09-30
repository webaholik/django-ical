#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-ical',
    version='1.6',
    description="iCal feeds for Django based on Django's syndication feed framework.",
    long_description='\n'.join([
        open('README.rst', encoding='utf-8').read(),
        open('CHANGES.rst', encoding='utf-8').read(),
    ]),
    keywords='ical calendar django syndication feed',
    author='Ian Lewis',
    author_email='security@jazzband.com',
    maintainer='Jazzband',
    maintainer_email='security@jazzband.com',
    license='MIT License',
    url='https://github.com/jazzband/django-ical',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Environment :: Plugins',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'Django>=1.11',
        'icalendar>=4.0.3',
        'django-recurrence>=1.10.0',
    ],
    packages=find_packages(),
    test_suite='tests.main',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)
