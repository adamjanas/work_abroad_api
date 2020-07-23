from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import mixins
from api.core.mixins import ActionPermissionMixin
from django_filters import rest_framework as filters
from api.core.permissions import IsAuthor, IsApplicant

from api.structure.models import (
    Offer,
    Application,
    UserReview,
    OfferReview
)
from api.structure.serializers import (
    OfferSerializer,
    ApplicationSerializer,
    UserReviewSerializer,
    OfferReviewSerializer
)


class OfferViewSet(ActionPermissionMixin, viewsets.ModelViewSet):
    permission_classes_by_action = {
        "default": (IsAuthenticated,),
        "update": (IsAuthor,),
        "partial_update": (IsAuthor,),
        "destroy": (IsAuthor,),
    }
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()
    filter_fields = {
        'author': ['exact'],
        'title': ['exact', 'contains'],
        'content': ['contains']
    }

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ApplicationViewSet(ActionPermissionMixin, viewsets.ModelViewSet):
    permission_classes_by_action = {
        "default": (IsAuthenticated,),
        "update": (IsApplicant,),
        "partial_update": (IsApplicant,),
        "destroy": (IsApplicant,),
    }
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    filter_fields = {
        'applicant': ['exact'],
        'title': ['exact', 'contains'],
        'content': ['contains']
    }

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)


class UserReviewViewSet(ActionPermissionMixin, viewsets.ModelViewSet):
    permission_classes_by_action = {
        "default": (IsAuthenticated,),
        "update": (IsAuthor,),
        "partial_update": (IsAuthor,),
        "destroy": (IsAuthor,),
    }
    serializer_class = UserReviewSerializer
    queryset = UserReview.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class OfferReviewViewSet(ActionPermissionMixin, viewsets.ModelViewSet):
    permission_classes_by_action = {
        "default": (IsAuthenticated,),
        "update": (IsAuthor,),
        "partial_update": (IsAuthor,),
        "destroy": (IsAuthor,),
    }
    serializer_class = OfferReviewSerializer
    queryset = OfferReview.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
