from os import name
from django.shortcuts import render,redirect,reverse
import random
from django.db.models import Max,Min
from django.contrib import *
from django.contrib.auth.models import User
from django.views.generic import (DetailView,FormView,ListView,TemplateView,UpdateView)
from django.contrib.auth.decorators import login_required
from .models import Item,itemHistory,Payment,Category
import datetime

# Create your views here.


def home(request):
    return render(request,'Home.html')

def Aboutus(request):
    return render(request,'Aboutus.html')

def Listitem(request):
    cat = request.GET['category']
    if cat == "Colourful":
        title = "COLOURFUL"
        some_colour = Category.objects.get(category="Colourful")
        Item_colour = Item.objects.all().filter(category=some_colour).order_by('name')
        context = {'Item': Item_colour,'title' : title}   
 
    else:
        title = "EARTH TONES"
        some_Earthtones = Category.objects.get(category="Earthtones")
        Item_Earthtones = Item.objects.all().filter(category=some_Earthtones).order_by('name')
        context = {'Item': Item_Earthtones,'title' : title}
        
    return render(request,'Category.html',context=context)

def Random(request):
    return render(request,'Random.html')

def Open(request):
    tone = request.GET['Tone']
    messages.info(request,"Double tap for Surprise") 
    if tone == "Earthtones":
        return render(request,'OpenEarthtone.html')
    elif tone == "Colourful":
        return render(request,'OpenColourful.html')

def Detail(request):
    type=request.GET['type']
    if request.user.is_authenticated:
        tracknum =  "KE " + str(random.randint(100000000, 1000000000))+ " TH"

        if type == "Earthtones":
            randomItem = Item.objects.filter(category=1).order_by('?')[:1]
        elif type == "Colourful":
            randomItem = Item.objects.filter(category=2).order_by('?')[:1]
        history = itemHistory(user=request.user , item=randomItem[0],date=datetime.datetime.now(),trackNum=tracknum)
        history.save()
        messages.info(request,"Thank you! Hope you like the prize") 
        context = {'Item': randomItem} 
        return render(request,'Detail.html',context=context)
    else:
        messages.info(request,"Please Login Before Try to Random") 
        return redirect('/Login')

@login_required(login_url='Login')
def Payments(request):
    if request.method == "POST":
        name = request.POST['name']
        numcard = request.POST['numcard']
        expire = request.POST['expires']
        cvv = request.POST['cvv']
        p = Payment(user=request.user,name=name,Numcard=numcard,expire=expire,cvv=cvv)
        p.save()
        messages.info(request,"Sucessful")
        return redirect('/')
    return render(request,'Payment.html')


class SearchItemListView(ListView):
    template_name = "Home.html"
    model = Item

    def get_queryset(self):
        queryset = super(SearchItemListView, self).get_queryset()
        q = self.request.GET.get("q")
        if q:
            item_by_name = queryset.filter(name__contains=q)
            item_by_category = queryset.filter(category__contains=q)
            return item_by_name | item_by_category
        return queryset



