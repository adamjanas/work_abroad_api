from rest_framework import serializers
from api.users.models import User
from api.structure.models import (
    Offer,
    Application,
    UserReview,
    OfferReview
)


class OfferSerializer(serializers.ModelSerializer):

    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Offer
        fields = ['id', 'title', 'author', 'content', 'period', 'salary', 'country']


class ApplicationSerializer(serializers.ModelSerializer):

    author = serializers.PrimaryKeyRelatedField(read_only=True)
    offer = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Offer.objects.all())

    class Meta:
        model = Application
        fields = ['id', 'offer', 'author', 'title', 'content']


class UserReviewSerializer(serializers.ModelSerializer):

    author = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=False, queryset=User.objects.all())

    class Meta:
        model = UserReview
        fields = ['id', 'user', 'author', 'title', 'content', 'review']


class OfferReviewSerializer(serializers.ModelSerializer):

    author = serializers.PrimaryKeyRelatedField(read_only=True)
    offer = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Offer.objects.all())

    class Meta:
        model = OfferReview
        fields = ['id', 'offer', 'author', 'title', 'content', 'review']
