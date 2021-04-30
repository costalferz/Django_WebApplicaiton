from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#from .views import *
from item import views
urlpatterns = [
    path('',views.home,name='home'),
    path('Aboutus',views.Aboutus,name='aboutus'),
    path('Colorful',views.Colourful,name='colourful'),
    path('Earthtone',views.Earthtone,name='earthtone'),
    path('Random',views.Random,name='random'),
    path('OpenEarthtone',views.OpenEarthtone,name='openearthtone'),
    #path('Colorful',views.Colorful,name='colorful'),
    #path('Colorful',views.Colorful,name='colorful'),
    #path('Colorful',views.Colorful,name='colorful'),
    #path('Colorful',views.Colorful,name='colorful'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
