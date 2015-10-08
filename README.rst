Django-email-blacklist
======================

Python class to detect Disposable Emails. Checks each email against a blacklist of ~890 domains used by various disposable email services. Tested in production with Django. This package requires Python 3, for Python 2.7 support `see here. <https://github.com/aaronbassett/DisposableEmailChecker>`__

Installation
------------

Install it using ``pip`` and add it to  your Django INSTALLED_APPS::
    
    $ pip install django-email-blacklist
    
Create a folder in your templates directory and download the example email blacklist::

    $ wget https://raw.github.com/zeioth/django-email-blacklist/master/disposable_email_domains.txt

Add this to to your ``settings.py``::

    DISPOSABLE_EMAIL_DOMAINS = "/path_to_your/disposable_email_domains.txt"

Usage
--------

To use the checker in your own scripts::

    >>> from django_email_blacklist import DisposableEmailChecker
    
    >>> email_checker = DisposableEmailChecker()
    >>> email_checker.is_disposable("foo@guerrillamail.com")
    True

Credits
--------
This is a fork from DisposableEmailChecker by aaronbassett, maintained by Zeioth.
