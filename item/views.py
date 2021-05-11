from django.shortcuts import render,redirect,reverse
import random
from django.contrib import *
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

def Open(request):
    c = request.GET['Tone']
    if c == "Earthtones":
        return render(request,'OpenEarthtone.html')
    elif c == "Colourful":
        return render(request,'OpenColourful.html')

def Detail(request):
    type=request.GET['type']
    if request.user.is_authenticated:
        if type == "Earthtones":
            some_Earthtones = Category.objects.get(category="Earthtones")
            Item_Earthtones = list(Item.objects.all().filter(category=some_Earthtones))
            randomItemE = random.sample(Item_Earthtones,1)
            context = {'Item': randomItemE}
        elif type == "Colourful":
            some_Colourful = Category.objects.get(category="Colourful")
            Item_Colourful = list(Item.objects.all().filter(category=some_Colourful))
            randomItemC = random.sample(Item_Colourful,1)
            context = {'Item': randomItemC}
        return render(request,'Detail.html',context=context)
    else:
        messages.info(request,"Login Before Random please") 
        return redirect('/Login')
        
# class ItemDetailView(DetailView):
#     model = Item
#     template_name = "Detail.html"

#     def get_success_url(self):
#         return reverse('Detail', kwargs={'slug': self.object.slug})

@login_required(login_url='Login')
def Payment(request):
    return render(request,'Payment.html')





@login_required(login_url='Login')
def tracking(request):
    context = {}
    return render(request,'Tracking.html')

@login_required(login_url='Login')
def newpass(request):

    if request.method == "POST":
        password=request.POST['password']
        repassword=request.POST['repassword']
        if password==repassword:
            pass
        else:
            messages.info(request,"password doesn't match") 
    return render(request,'Newpass.html') 

@login_required(login_url='Login')
def accountprofile(request):
    context = {}
    return render(request,'Account Profile.html') 

@login_required(login_url='Login')
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