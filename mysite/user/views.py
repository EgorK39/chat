from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from chat.models import Room

from .models import UserModel
from .permissions import IsAdminOrReadOnly, IsUserOrReadOnly
from .serializers import UserSerializer, UserUserSerializer


class ProfileAPIList(generics.ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProfileAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly,)


class ProfileAPIDelete(generics.RetrieveDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly,)


class UserUpAPIList(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUserSerializer


class UserAPIList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserUserSerializer

# class Profile(mixins.CreateModelMixin,
#               mixins.RetrieveModelMixin,
#               mixins.UpdateModelMixin,
#               mixins.DestroyModelMixin,
#               mixins.ListModelMixin,
#               GenericViewSet):
#     # queryset = UserModel.objects.all()
#     serializer_class = UserSerializer
#
#     def get_queryset(self):
#         return UserModel.objects.all()
#
#     # def get_queryset(self):
#     #     pk = self.kwargs.get('pk')
#     #     if not pk:
#     #         return UserModel.objects.all()
#     #     return UserModel.objects.filter(pk=pk)
#
#     @action(methods=['get'], detail=True)
#     def rooms(self, request, pk=None):
#         rooms = Room.objects.get(pk=pk)
#         host = Room.objects.get(pk=pk).host.user.username
#
#         return Response({'room': rooms.name, 'host': host})
