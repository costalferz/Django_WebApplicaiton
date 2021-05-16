from os import name
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from item import views
from .views import *
urlpatterns = [
    path('',views.home,name='home'),
    path('Aboutus',views.Aboutus,name='aboutus'),
    path('List',views.Listitem),
    path('Random',views.Random,name='random'),
    #path('product/<slug:slug>',ItemDetailView.as_view(),name='Detail'),
    path('ProductDetail' , views.Detail,name='Detail'),
    path('Payment' , views.Payments),
    path('Search' , SearchItemListView.as_view(),name='search'),
    path('Open',views.Open,name='open'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

