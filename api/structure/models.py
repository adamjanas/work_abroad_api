from django.db import models
from api.users.models import User
from django.utils import timezone
from django_countries.fields import CountryField
import datetime

class Offer(models.Model):
    title = models.CharField(max_length=80)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    start_date = models.DateField(default=datetime.date.today())
    finish_date = models.DateField(default=datetime.date.today())
    salary = models.DecimalField(max_digits=8, decimal_places=2)
    country = CountryField()
    offer_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.title} - {self.author}"


class Application(models.Model):
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    attachment = models.FileField(help_text='attach your cv')
    application_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.offer} - {self.title}"


class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    review = models.IntegerField(help_text='Select review from 1 to 10. \'1\' is the smallest one.')

    def __str__(self):
        return f"{self.user} - {self.title} "


class OfferReview(models.Model):
    offer = models.ForeignKey('Offer', on_delete=models.CASCADE, related_name='offer_reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80)
    content = models.TextField()
    review = models.IntegerField(help_text='Select review from 1 to 10. \'1\' is the smallest one.')

    def __str__(self):
        return f"{self.offer} - {self.title}"
