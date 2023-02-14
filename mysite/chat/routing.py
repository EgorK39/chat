from django.urls import re_path

from . import consumers

"""
Мы вызываем метод класса as_asgi(), чтобы получить приложение ASGI, 
которое будет создавать экземпляр нашего потребителя для каждого пользовательского соединения. 
Это похоже на функцию as_view() в Django, 
которая играет ту же роль для экземпляров представления Django по запросу.
"""

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),

]
