from django.db import models
from api.users.models import User
from api.core.models import CreatedAtAbstractModel


class Message(CreatedAtAbstractModel):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    attachment = models.FileField(null=True, blank=True)

