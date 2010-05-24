Django Contact:
===============
**Django contact app.**


Dependancies:
=============
django-options
    git@github.com:praekelt/django-options.git


Models:
=======

ContactOptions:
---------------
class models.ContactOptions
    
Add a site-wide contact details to the CMS, Link contact form recipients via Foreign key to Users.

API Reference:
~~~~~~~~~~~~~~

FIELDS
******
telephone
    Date field to specify the date the competition should start being displayed.
fax
    Date field to specify the date the competition should stop being displayed.
physical_address
    Char field for a short question specific to the competition which should be answered correctly to qualify as a winner.
postal_address
    Char field for a short question specific to the competition which should be answered correctly to qualify as a winner.
postal_address
    Char field for a short question specific to the competition which should be answered correctly to qualify as a winner.
email
    Date field to specify the date the competition should stop being displayed.
sms
    Date field to specify the date the competition should stop being displayed.
email_recipients
    Date field to specify the date the competition should stop being displayed.

METHODS
*******
None

MANAGERS
********
None


Tag Reference
=============

Inclusion Tags
--------------
None

Template Tags
-------------
None
