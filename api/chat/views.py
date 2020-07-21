from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import mixins
from api.core.mixins import ActionPermissionMixin
from api.core.permissions import IsAuthor
from api.chat.models import Message
from api.chat.serializers import MessageSerializer
from django_filters import rest_framework as filters


class MessageViewSet(ActionPermissionMixin, viewsets.ModelViewSet):
    permission_classes_by_action = {
        "default": (IsAuthenticated,),
        "update": (IsAuthor,),
        "partial_update": (IsAuthor,),
        "destroy": (IsAuthor,)
    }
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
    filter_fields = {
        'sender': ['exact'],
        'content': ['contains']
    }

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


