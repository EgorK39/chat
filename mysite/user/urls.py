from django.contrib import admin
from django.urls import path, include
from .views import (
    ProfileAPIList, ProfileAPIUpdate, ProfileAPIDelete, UserUpAPIList, UserAPIList
)
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'profile', Profile, basename='profile')
# print(router.urls)

urlpatterns = [
    path('profile/', ProfileAPIList.as_view()),
    path('profile/<int:pk>/', ProfileAPIUpdate.as_view()),
    path('profile/<int:pk>/delete/', ProfileAPIDelete.as_view()),
    path('userlist/', UserAPIList.as_view()),
    path('userlist/<int:pk>/', UserUpAPIList.as_view()),
    path('drf-auth/', include('rest_framework.urls')),

]
