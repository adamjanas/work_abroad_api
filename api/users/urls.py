from django.contrib import admin
from django.urls import path
from api.users.views import UserCreate

urlpatterns = [
    path('register', UserCreate.as_view(), name='register'),
]
