from rest_framework import serializers
from user.models import Profile


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email',
                  'phone_number', 'age', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Profile.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name', 'email',
                  'phone_number', 'age', 'password')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name',
                  'phone_number', 'age', 'username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number', 'age']
        extra_kwargs = {
            'username': {'read_only': True},
            'email': {'required': True},
        }
