from django.contrib.auth.models import User
from django.db import models

from preferences.models import Preferences
        
class ContactPreferences(Preferences):
    __module__ = 'preferences.models'
    
    telephone = models.CharField(
        max_length=24,
        blank=True,
        null=True,
    )
    fax = models.CharField(
        max_length=24,
        blank=True,
        null=True,
    )
    physical_address = models.TextField(
        blank=True,
        null=True,
    )
    postal_address = models.TextField(
        blank=True,
        null=True,
    )
    email = models.EmailField(
        blank=True,
        null=True,
    )
    sms = models.CharField(
        max_length=24,
        blank=True,
        null=True,
    )
    email_recipients = models.ManyToManyField(
        User,
        blank=True,
        null=True,
        help_text='Select users who will recieve emails sent via the general contact form.'
    )
    
    class Meta:
        verbose_name = 'Contact preferences'
        verbose_name_plural = 'Contact preferences'
