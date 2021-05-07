from django.shortcuts import redirect, render,get_object_or_404
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ( CreateView, FormView, TemplateView)

from .form import UserRegisterForm
# Create your views here.
class SignUpView(CreateView):
    form_class = UserRegisterForm
    success_url = reverse_lazy('login')
    template_name = 'Signup.html'

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
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'Login.html')

def logout_view(request):
    auth.logout(request)
    return render(request, 'Login.html')

def register(request):
    return render(request, 'register.html')

def registration(request):
    username = request.POST['username']
    password=request.POST['password']
    repassword=request.POST['repassword']
    mobile = request.POST['mobile']
    email = request.POST['email']
    mobile = request.POST['mobile']
    firstname = request.POST['firstname']
    # lastname = request.POST['lastname']
    # city = request.POST['city']
    # city = city.lower()
    # pincode = request.POST['pincode']
    try:
        user = User.objects.create_user(username = username, password = password, email = email)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
    except:
        return render(request, 'customer/registration_error.html')
    try:
        area = Area.objects.get(city = city, pincode = pincode)
    except:
        area = None
    if area is not None:
        customer = Customer(user = user, mobile = mobile, area = area)
    else:
        area = Area(city = city, pincode = pincode)
        area.save()
        area = Area.objects.get(city = city, pincode = pincode)
        customer = Customer(user = user, mobile = mobile, area = area)

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


