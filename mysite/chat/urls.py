from django.urls import path

from . import views
# from .views import index, room

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]

# urlpatterns = [
#     path('', index, name='index'),
#     path('<str:room_name>/', room, name='room'),
# ]
