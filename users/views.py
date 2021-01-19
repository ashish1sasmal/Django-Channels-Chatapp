from django.shortcuts import render,redirect, reverse

from django.contrib import messages

from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.views.generic import View
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import *
import cloudinary

# Create your views here.

def home(request):
	return render(request,"users/home.html")

@login_required
def user_logout(request):
    logout(request)
    messages.success(request,"You have been logged out!")
    return redirect('home')

class EditProfile(LoginRequiredMixin, View):
    def get(self,request,*args,**kwargs):
        profile = Profile.objects.get(user=request.user)
        print(profile)
        return render(request,"users/edit_profile.html",{"profile":profile})

    def post(self,request,*args,**kwargs):
        first = request.POST.get("first")
        last = request.POST.get("last")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("first")

        user = User.objects.get(id=request.user.id)
        user.first_name=first
        user.last_name = last
        user.email = email
        user.set_password = password
        user.save()
        print("User data changed!")
        profile = Profile.objects.get(user=request.user)
        profile.phone = phone
        print(request.FILES['image'])
        out = cloudinary.uploader.upload(request.FILES['image'])
        print(out)
        profile.image = out['secure_url']
        profile.save()
        print("Profile data changed!")
        messages.success(request,"Your changes saved!")
        return HttpResponseRedirect(reverse('profile', kwargs={'name': request.user.username}))


class UserProfile(LoginRequiredMixin, View):
    def get(self,request,*args,**kwargs):
        user = User.objects.get(username=kwargs["name"])
        isFriend=True
        # print(Friends.objects.all())
        friendlist = Friends.objects.filter(Q(user1__user=user)|Q(user2__user=user))
        profile = user.profile
        fl=[]
        for i in friendlist:
            if i.user1.user.username == user.username:
                fl.append(i.user2)
            else:
                fl.append(i.user1)
        print(fl)
        if Friends.objects.filter(user1__user__username=user.username,user2__user__username=request.user.username).count()==0 and Friends.objects.filter(user2__user__username=user.username,user1__user__username=request.user.username).count()==0:
            isFriend=False
        return render(request,"users/profile.html",{"user":user,"isFriend":isFriend,'fl':fl,'profile':profile})



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
		pro.image = "https://res.cloudinary.com/dqgww23zy/image/upload/v1611039496/default_qcqui4.jpg"
		pro.save()
		return redirect('login')

class Friendlist(View):
	def get(self,request,*args,**kwargs):
		users = User.objects.exclude(id=request.user.id)
		return render(request,"users/friends.html",{"users":users})
