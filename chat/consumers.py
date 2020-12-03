import json
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import *
from django.contrib.auth.models import User

from channels.db import database_sync_to_async

#

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json['username']
        print(message,username)
        # print(User.objects.all())

        await self.saveM(username,message,self.room_group_name)

        print("Message Saved!")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
            }
        )

    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))

    @database_sync_to_async
    def saveM(self,username,message,room_group_name):
        print(username,message,room_group_name)
        user = User.objects.get(username=username)
        group = ChatGroup.objects.get(groupname = room_group_name)
        newM = Message(text=message,fromUser=user,toGroup=group)
        newM.save()


    pass