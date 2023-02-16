from rest_framework import serializers
from .models import UserModel, User


class UserSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserModel
        fields = [
            'user',
            'photo',
            'about',
        ]


class UserUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
        ]
#
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
