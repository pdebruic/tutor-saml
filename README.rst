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


Credits
-------

https://discuss.overhang.io/t/sso-missing-backends-how-do-i-enable-them/251/5


Notes
------

OK so I was using the binary tutor so havent tested this plugin.  I did make a YAML plugin that worked for me for our IdP.  When using these settings anyone that clicks on the login or register link is redirected to yoru site and then an account is automatically created for them (if needed) and they're given access.    

```
name: saml
version: 0.1.0
patches:
 common-env-features: |
    "ENABLE_COMBINED_LOGIN_REGISTRATION" : true,
    "ENABLE_THIRD_PARTY_AUTH" : true,
    "THIRD_PARTY_AUTH_HINT" : "saml-YOURSAMLIDPSLUG",
    "ENABLE_UNICODE_USERNAME" : true

 openedx-common-settings: |
    # saml special settings
    THIRD_PARTY_AUTH_BACKENDS = "third_party_auth.saml.SAMLAuthBackend"
```


License
-------

This software is licensed under the terms of the AGPLv3.
