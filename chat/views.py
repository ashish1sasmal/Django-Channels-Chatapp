from django.shortcuts import render

from .models import *


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
	groupmsgs = Message.objects.filter(toGroup__groupname = room_name).order_by('-timestamp')
	print(groupmsgs)
	return render(request, 'chat/chatroom.html', {
        'room_name': room_name,
        'groupmsgs':groupmsgs
    })