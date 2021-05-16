#from os import add_dll_directory
import users
from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ( CreateView, FormView, TemplateView)
from django.contrib.auth.decorators import login_required
from .form import ProfileForm
from .models import Profile
from item.models import Item,itemHistory,Payment,Category
# Create your views here.

def Loginform(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session.set_expiry(600)
                messages.info(request,"Welcome to Elon Mysterious box Feel free to random.") 
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.info(request,"Please Try to Login Again.") 
                return redirect('/Login')
        else:
            messages.info(request,"Please Register Before Try to Login") 
            return redirect('/Login')
            
    else:
        return render(request, 'Login.html')

def Logout_view(request):
    auth.logout(request)
    messages.info(request,"You are now Logged Out ") 
    return redirect('/Login')

def Register(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        repassword=request.POST['repassword']
        if password==repassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"This User id has already been registered.")
                return redirect('/Register')
            elif  User.objects.filter(email=email).exists():
                messages.info(request,"This email has already been registered.")
                return redirect('/Register')
            else:
                new_user= User.objects.create_user(username=username,password=password, email=email,)
                profile = Profile.objects.create(user=new_user)
                profile.save()
                new_user.save()
                auth.login(request,new_user,backend='django.contrib.auth.backends.ModelBackend')
                messages.info(request,"Welcome to Elon Mysterious box Feel free to random.")
                return redirect('/')
        else:
            messages.info(request,"Password doesn't match")
            return redirect('/Register')
    else:
        return render(request, 'Signup.html')

@login_required(login_url='Login')
def Myorder(request):
    
    tablehistory = itemHistory.objects.filter(user=request.user).order_by("-date")[:5]
    context = {'history' : tablehistory}
    return render(request,'Myorder.html',context=context,)


@login_required(login_url='Login')
def Newpass(request):
    if request.method == "POST":
        password=request.POST['password']
        repassword=request.POST['repassword']
        if password==repassword:
            u = User.objects.get(username=request.user.username)
            u.set_password(password)
            u.save()
            return redirect('/Myorder')
        else:
            messages.info(request,"password doesn't match") 
            return redirect("/Newpass")
    return render(request,'New-pass.html') 

@login_required(login_url='Login')
def Accountprofile(request):
    if request.method == "POST":
        user=request.POST['username']
        email=request.POST['email']
        if User.objects.filter(username=user).exists():
            messages.info(request,"Username already used")
            return redirect('/Accountprofile')
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email already used")
            return redirect('/Accountprofile')
        else:
            update_user = request.user
            update_user.username=user
            update_user.email=email
            update_user.save()
            messages.info(request,"Update Account Profile Sucessful")
            return HttpResponseRedirect('/Myorder')
    return render(request,'Account Profile.html') 

@login_required(login_url='Login')
def Address(request):
    if request.method == "POST":
        phone_num=request.POST['telnum']
        address=request.POST['address']
        Contact = Profile.objects.filter(user=request.user).update(phone_num=phone_num,address=address)
        messages.info(request,"Update Contact Sucessful")
        return HttpResponseRedirect('/Myorder') 
    return render(request,'Address.html') 

from django.core.files.storage import FileSystemStorage
@login_required(login_url='Login')
def UpdateProfile(request):
    if request.method == "POST" and request.FILES.get('photo'):
        image = request.FILES.get('photo')
        fs = FileSystemStorage()
        image_fs = fs.save(image.name, image)
        image_new = Profile.objects.filter(user=request.user).update(image=image_fs)
        messages.info(request,"Update Profile Sucessful")
        return redirect('/Myorder')
    return render(request,'UpdateProfile.html')