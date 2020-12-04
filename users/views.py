from django.shortcuts import render,redirect

from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.views.generic import View
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Q

from .models import *

# Create your views here.

def home(request):
	return render(request,"users/home.html")

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


class UserProfile(LoginRequiredMixin, View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(username=kwargs["name"])
        isFriend=True
        # print(Friends.objects.all())
        friendlist = Friends.objects.filter(Q(user1__user=user)|Q(user2__user=user))
        fl=[]
        for i in friendlist:
            if i.user1.user.username == user.username:
                fl.append(i.user2)
            else:
                fl.append(i.user1)
        print(fl)
        if Friends.objects.filter(user1__user__username=user.username,user2__user__username=request.user.username).count()==0 and Friends.objects.filter(user2__user__username=user.username,user1__user__username=request.user.username).count()==0:
            isFriend=False
        return render(request,"users/profile.html",{"user":user,"isFriend":isFriend,'fl':fl})



class Userlogin(View):
    def get(self,request,*args,**kwargs):
        return render(request,"users/login.html")

    def post(self,request,*args,**kwargs):
    	username = request.POST.get('username')
    	password = request.POST.get('password')
    	print(username,password)
    	user=authenticate(username=username,password=password)
    	if user:
    		login(request,user)
    		messages.success(request,"You have been logged in!")
    		print("logged in")
    		return redirect('home')
    	else:
    		messages.warning(request,'Wrong input!')
    		return render(request,"users/login.html")


class Signup(View):
	def get(self,request,*args,**kwargs):
		return render(request,"users/signup.html")

	def post(self,request,*args,**kwargs):
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = User.objects.create_user(username=username,email=email,password=password)
		pro = Profile(user=user)
		pro.save()
		return redirect('login')

class Friendlist(View):
	def get(self,request,*args,**kwargs):
		users = User.objects.exclude(id=request.user.id)
		return render(request,"users/friends.html",{"users":users})