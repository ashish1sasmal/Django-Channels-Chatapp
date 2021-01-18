from django.urls import re_path, path

from . import consumers

websocket_urlpatterns = [
    path('ws/profile/<str:name>/', consumers.ProfileConsumer.as_asgi()),
]
