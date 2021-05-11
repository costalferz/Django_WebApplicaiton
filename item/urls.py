from os import name
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from item import views
from .views import *
urlpatterns = [
    path('',views.home,name='home'),
    path('Aboutus',views.Aboutus,name='aboutus'),
    path('Colourful',views.Colourful,name='colourful'),
    path('Earthtone',views.Earthtone,name='earthtone'),
    path('Random',views.Random,name='random'),
    #path('product/<slug:slug>',ItemDetailView.as_view(),name='Detail'),
    path('ProductDetail' , views.Detail,name='Detail'),
    path('Payment' , views.Payment),
    path('Open',views.Open,name='open'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

