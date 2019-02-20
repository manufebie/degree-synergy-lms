from django.conf import settings
from django.contrib import AbstractUser
from django.db import models


class User(AbstractUser):
    '''
    Implementing multiple roles for users by inheriting from Django's "AbstractUser" model
    by adding boolean fields.
    '''
    is_admin = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)


class Client(models.Model):
    '''
    Client model: base class.
    '''
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)

    def _str__(self):
        return self.name



