from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ( CreateView, FormView, TemplateView)
from django.contrib.auth.decorators import login_required
from .form import UserRegisterForm
from .models import Profile
# Create your views here.

def Loginform(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session.set_expiry(300)
                messages.info(request,"Login Sucuessful") 
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.info(request,"Please Login Again.") 
                return redirect('/Login')
        else:
            messages.info(request,"Please Try to Login Again ") 
            return redirect('/Login')
            
    else:
        return render(request, 'Login.html')

def Logout_view(request):
    auth.logout(request)
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
                url = '/default.png'
                new_user= User.objects.create_user(username=username,password=password, email=email,)
                new_user.save()
                auth.login(request,new_user)
                messages.info(request,"Login Sucessful.")
                return redirect('/')
        else:
            messages.info(request,"password doesn't match")
            return redirect('/Register')
    else:
        return render(request, 'Signup.html')

@login_required(login_url='Login')
def Myorder(request):
    # if user got column in data base
    current_user = request.user
    profile = Profile.objects.all()#(user=current_user)
    context = {'pro' : profile}
    return render(request,'Myorder.html',context=context,)

@login_required(login_url='Login')
def Newpass(request):
    current_user = request.user
    if request.method == "POST":
        password=request.POST['password']
        repassword=request.POST['repassword']
        if password==repassword:
            u = User.objects.get(username=current_user)
            u.set_password(password)
            u.save()
            return redirect('/Myorder')
        else:
            messages.info(request,"password doesn't match") 
    return render(request,'Newpass.html') 

@login_required(login_url='Login')
def Accountprofile(request):
    context = {}
    return render(request,'Account Profile.html') 

@login_required(login_url='Login')
def Address (request):
    context = {}
    return render(request,'Address.html') 

@login_required(login_url='Login')
def UpdateProfile(request):
    if request.method == "POST":
        image = request.POST['image']
    return render(request,'UpdateProfile.html')
