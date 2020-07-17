from django.db import models
from api.users.models import User
from django.utils import timezone


class Message(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    attachment = models.FileField(null=True, blank=True, help_text='attach some files')
    message_date = models.DateTimeField(default=timezone.now())
