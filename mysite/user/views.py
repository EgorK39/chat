from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import mixins, generics, views, status, permissions
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
)
from django.http import Http404

from chat.models import Room

from .models import UserModel
from .permissions import IsAdminOrReadOnly, IsUserOrReadOnly
from .serializers import UserListSerializer, UserSerializer


class ProfileAPIList(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ProfileAPIDetail(views.APIView):
    # permission_classes = IsUserOrReadOnly
    # def get_permissions(self):
    #     # def get_permissions(self, request, view, obj):
    #     # Read permissions are allowed to any request,
    #     # so we'll always allow GET, HEAD or OPTIONS requests.
    #     if self.request.method in permissions.SAFE_METHODS:
    #         return True
    #
    #     # Instance must have an attribute named `owner`.
    #     return super(ProfileAPIDetail, self).get_permissions()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(kwargs)
    #     self.action = None
    #

    def get_object(self, pk):
        try:
            return UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = UserModel.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class ProfileAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = UserListSerializer
#     permission_classes = (IsUserOrReadOnly,)


#
# class ProfileAPIDelete(generics.RetrieveDestroyAPIView):
#     queryset = UserModel.objects.all()
#     serializer_class = UserListSerializer
#     permission_classes = (IsAdminOrReadOnly,)

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
