from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from api.users.models import User
from api.users.serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    """
    User's creation
    """
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


