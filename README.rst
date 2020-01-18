Enable SAML plugin for `Tutor <https://docs.tutor.overhang.io>`__
===================================================================================

Installation
------------

::

    pip install git+https://github.com/pdebruic/tutor-saml

Usage
-----

::

    tutor plugins enable saml
    
then

::

    tutor local run lms bash

then

::  

    ./manage.py lms saml --pull --settings=tutor.production


License
-------

This software is licensed under the terms of the AGPLv3.
