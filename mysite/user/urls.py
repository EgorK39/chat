from django.contrib import admin
from django.urls import path, include
from .views import (
    ProfileAPIList, ProfileAPIDetail
)
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'profile', Profile, basename='profile')
# print(router.urls)

urlpatterns = [
    path('profiles/', ProfileAPIList.as_view(), name='profiles'),
    path('profiles/<int:pk>/', ProfileAPIDetail.as_view(), name='profile'),

]
