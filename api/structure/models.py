from django.db import models
from api.users.models import User
from django.utils import timezone
from django_countries.fields import CountryField


class Offer(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    period = models.CharField(max_length=18, help_text='e.g (1 month, 6 months, 1 year)')
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    country = CountryField()
    offer_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class Application(models.Model):
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField
    content = models.TextField()
    application_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.offer} - {self.title}"
