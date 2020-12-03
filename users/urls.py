from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('login/',views.Userlogin.as_view(),name='login'),
    path('signup/',views.Signup.as_view(),name='signup'),
    path('logout/',views.user_logout,name="logout"),
    path('flist',views.Friends.as_view(),name="list")
   ]