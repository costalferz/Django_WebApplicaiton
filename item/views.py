from django.shortcuts import render,redirect,reverse
import random
from django.db.models import Count
from django.contrib.auth.models import User
from django.views.generic import (DetailView,FormView,ListView,TemplateView,UpdateView)
from django.contrib.auth.decorators import login_required
from .models import Item,itemHistory,Payment,Category
# Create your views here.


def home(request):
    return render(request,'Home.html')

def Aboutus(request):
    return render(request,'Aboutus.html')


def Colourful(request):
    some_colour = Category.objects.get(category="Colourful")
    Item_colour = Item.objects.all().filter(category=some_colour).order_by('-name')
    context = {'Item_co': Item_colour}
    return render(request,'Colourful.html',context)

def Earthtone(request):
    some_Earthtones = Category.objects.get(category="Earthtones")
    Item_Earthtones = Item.objects.all().filter(category=some_Earthtones).order_by('-name')
    context = {'Item_Earth': Item_Earthtones}
    return render(request,'EarthTone.html',context=context)

def Random(request):
    return render(request,'Random.html')

def OpenEarthtone(request):
    return render(request,'OpenEarthtone.html')

def OpenColourful(request):
    return render(request,'OpenColourful.html')


# def RandomTone(request):
#     template_name = 'index.html'
#     model = Item


def Detail(request):
    context = {}
    return render(request,'Detail.html')

def tracking(request):
    context = {}
    return render(request,'Tracking.html')

def newpass(request):
    context = {}
    return render(request,'Newpass.html') 

def accountprofile(request):
    context = {}
    return render(request,'Account Profile.html') 

def address (request):
    context = {}
    return render(request,'Address.html') 

class SearchItemListView(ListView):
    template_name = "Colourful.html"
    model = Item

    def get_queryset(self):
        queryset = super(SearchItemListView, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            item_by_name = queryset.filter(name__icontains=q)
            item_by_category = queryset.filter(category__icontains=q)
            return item_by_name | item_by_category
        return queryset