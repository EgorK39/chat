from rest_framework import serializers
from .models import UserModel
from django.contrib.auth.models import User


class UserListSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = UserModel
        fields = [
            'user',
            'photo',
            'about',
        ]


class UserSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = UserModel
        fields = [
            'user',
            'photo',
            'about',
        ]

# class UserSerializer(serializers.ModelSerializer):
#     user = serializers.CharField()
#     photo = serializers.ImageField()
#     about = serializers.CharField()
#
#     def create(self, validated_data):
#         return UserModel.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.photo = validated_data.get('photo', instance.photo),
#         instance.about = validated_data.get('about', instance.about)
#         instance.save()
#         return instance
