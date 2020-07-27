from rest_framework import serializers
from api.users.models import User
from api.chat.models import Message


class MessageSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    recipient = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ('id', 'recipient', 'author', 'content', 'attachment')
