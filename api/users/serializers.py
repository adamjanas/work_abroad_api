from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from api.users.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=28,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'birth_date', 'phone_number', 'sex')

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'],
                    birth_date=validated_data['birth_date'], phone_number=validated_data['phone_number'],
                    sex=validated_data['sex'])
        user.set_password((validated_data['password']))
        user.save()
        return user

