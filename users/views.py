from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ( CreateView, FormView, TemplateView)

from .form import UserRegisterForm
# Create your views here.

def Loginform(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.info(request,"Please Login Again.") 
                return redirect('/Login')
        else:
            messages.info(request,"Please Try to Login Again ") 
            return redirect('/Login')
            
    else:
        return render(request, 'Login.html')

def logout_view(request):
    auth.logout(request)
    return render(request, 'Login.html')

def register(request):
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
                new_user= User.objects.create_user(
                username=username,
                password=password,
                email=email,)
                new_user.save()
                auth.login(request,new_user)
                return redirect('/')
        else:
            messages.info(request,"password doesn't match")
            return redirect('/Register')
    else:
        return render(request, 'Signup.html')



# def Loginform(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     #check username, password
#     user = authenticate(username=username,password=password)
    
#     if user is not None:
#         auth.login(request,user)
#         return redirect('home')
#     else:
#         messages.info(request,"Doesn't Match Any Username or Password")
#         return redirect('Login.html')


