from django.db import models
from api.users.models import User
from api.core.constants import CreatedAt


class Message(CreatedAt):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    attachment = models.FileField(null=True, blank=True)

