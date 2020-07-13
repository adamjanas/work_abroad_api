from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from django_countries.fields import CountryField
from api.core.constants import SEX
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
    birth_date = models.DateTimeField(null=True, blank=True)
    phone_number = PhoneField(null=True, blank=True, help_text='Phone Number')
    country = CountryField(multiple=True)
    sex = models.CharField(max_length=6, choices=SEX.choices(), null=True)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)