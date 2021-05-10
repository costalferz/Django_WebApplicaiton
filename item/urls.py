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
    path('Openearthtone',views.OpenEarthtone,name='openearthtone'),
    path('Opencolourful',views.OpenColourful,name='opencolurful'),
    path('tracking',views.tracking,),
    path('newpass',views.newpass,),
    path('accountprofile',views.accountprofile,),
    path('address',views.address,),
    #path('Colorful',views.Colorful,name='colorful'),
    #path('Colorful',views.Colorful,name='colorful'),
    #path('Colorful',views.Colorful,name='colorful'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

