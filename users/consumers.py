# @Author: ASHISH SASMAL <ashish>
# @Date:   04-12-2020
# @Last modified by:   ashish
# @Last modified time: 04-12-2020



import json
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import *
from django.contrib.auth.models import User

from channels.db import database_sync_to_async



class ProfileConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("profile socket")
        self.room_name = self.scope['url_route']['kwargs']['name']
        self.room_group_name = self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        if action=="1":
            print("#")
            result = await self.addFriends(text_data_json["u1"],text_data_json["u2"])
            await self.channel_layer.group_send(
                        self.room_group_name,
                        {
                            'type': 'response',
                            'result': result
                        }
                    )
    async def response(self, event):
        message = event['result']

        await self.send(text_data=json.dumps({
            'result': result
        }))

    @database_sync_to_async
    def addFriends(self,u1,u2):
        print(u1,u2)
        print(User.objects.get(id=u1))
        u1 = Profile.objects.get(user__id=u1)
        u2 = Profile.objects.get(user__id=u2)
        fr = Friends(user1=u1, user2=u2)
        fr.save()
        print("We are friends!")
        return True

    pass
