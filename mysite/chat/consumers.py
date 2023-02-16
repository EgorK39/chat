import json
from channels.generic.websocket import AsyncWebsocketConsumer, \
    WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        print(f'Room - {self.room_name}', f'Gr - {self.room_group_name}')
        # Join room group

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,

        )
        print(f' Channel = {self.channel_name}')
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group

        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    """ Получать сообщение от WebSocket """

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print(f'Message receive - {message}')

        # Send message to room group

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        print(f'Message chat_message - {message}')

        # Send message to WebSocket

        await self.send(text_data=json.dumps({
            'message': message
        }))


""" синхронный стиль """
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         """ Области видимости """
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name
#         print(f'Room - {self.room_name}', f'Gr - {self.room_group_name}')
#         # Join room group
#
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name,
#
#         )
#         print(f' Channel = {self.channel_name}')
#         self.accept()
#
#     def disconnect(self, close_code):
#         # Leave room group
#
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
#
#     """ Получать сообщение от WebSocket """
#
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']
#         print(f'Message receive - {message}')
#
#         # Send message to room group
#
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )
#
#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']
#         print(f'Message chat_message - {message}')
#
#         # Send message to WebSocket
#
#         self.send(text_data=json.dumps({
#             'message': message
#         }))
