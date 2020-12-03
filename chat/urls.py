from django.urls import path

from . import views

urlpatterns = [
    path('<str:user2>/', views.room, name='room'),
]