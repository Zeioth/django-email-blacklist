Django-email-blacklist
======================

Python class for use with Django to detect Disposable Emails. Checks each email against a blacklist of ~890 domains used by various disposable email services.

Installation
------------

Install it using ``pip``::
    
    $ pip install django-email-blacklist
    
Create a folder in your templates directory and download the example email blacklist::

    $ wget https://raw.github.com/zeioth/django-email-blacklist/master/disposable_email_domains.txt

Add this to to your ``settings.py``::

    DISPOSABLE_EMAIL_DOMAINS = "/path_to_your/disposable_email_domains.txt"

Usage
--------

To use the checker in your own scripts::

    >>> from disposable_email_checker import DisposableEmailChecker
    
    >>> email_checker = DisposableEmailChecker()
    >>> email_checker.is_disposable("foo@guerrillamail.com")
    True

Credits
--------
This is a fork from DisposableEmailChecker by aaronbassett, mantained by Zeioth.