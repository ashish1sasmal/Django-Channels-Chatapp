from django.shortcuts import render

from .models import *
from django.contrib.auth.models import User
import random, string

def index(request):
    return render(request, 'chat/index.html', {})


def checkGroup(user1,user2):
	print(user1,user2)
	user1 = User.objects.get(username=user1)
	user2 = User.objects.get(username=user2)
	if ChatGroup.objects.filter(user1=user1, user2=user2).count()==0 and ChatGroup.objects.filter(user1=user2, user2=user1).count()==0:
		x = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
		g = ChatGroup(groupname=x, user1=user1, user2=user2)
		g.save()
		return x
	else:
		if ChatGroup.objects.filter(user1=user1, user2=user2).count()!=0:
			return ChatGroup.objects.get(user1=user1, user2=user2).groupname
		else:
			return ChatGroup.objects.get(user1=user2, user2=user1).groupname


def room(request, user2):
	
	# print(groupmsgs)
	# groupmsgs={}
	room_name = checkGroup(request.user.username, user2)
	group = ChatGroup.objects.get(groupname=room_name)
	groupmsgs = Message.objects.filter(toGroup = group).order_by('timestamp')
	print(room_name)
	return render(request, 'chat/chatroom.html', {
		'room_name':room_name,
        'groupmsgs':groupmsgs,
        'user2':user2
    })