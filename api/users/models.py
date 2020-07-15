from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from django_countries.fields import CountryField
from api.core.constants import Sex


class User(AbstractUser):
    birth_date = models.DateTimeField(null=True, blank=True)
    phone_number = PhoneField(null=True, blank=True, help_text='Phone Number')
    country = CountryField()
    sex = models.IntegerField(choices=Sex.choices(), null=True, blank=True)


