#!/usr/bin/env python

from setuptools import setup


setup(
    name="django-email-blacklist",
    packages=['django_email_blacklist'],
    version="1.0.1",
    license='MIT',
    author='Zeioth',
    author_email='test@gmail.com',
    description='Python class for use with Django to detect Disposable Emails.',
    keywords="django email blacklist disposable validation",
    install_requires='',
    include_package_data=True,
    url='https://github.com/Zeioth/django-email-blacklist',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
