from rest_framework import serializers
from api.users.models import User
from django.core.exceptions import ValidationError
import datetime
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
        fields = ['id', 'title', 'author', 'content', 'start_date', 'finish_date', 'salary', 'country']

    def validate(self, data):
        if data['start_date'] >= data['finish_date']:
            raise serializers.ValidationError('Starting date should be less than finishing date!')
        if data['start_date'] <= datetime.date.today() or data['finish_date'] <= datetime.date.today():
            raise ValidationError('The date cannot be today or in the past!')
        return data

class ApplicationSerializer(serializers.ModelSerializer):

    applicant = serializers.PrimaryKeyRelatedField(read_only=True)
    offer = serializers.PrimaryKeyRelatedField(read_only=False, queryset=Offer.objects.all())

    class Meta:
        model = Application
        fields = ['id', 'offer', 'applicant', 'title', 'content', 'attachment']


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
