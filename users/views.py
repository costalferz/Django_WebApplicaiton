from django.shortcuts import render,get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
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

