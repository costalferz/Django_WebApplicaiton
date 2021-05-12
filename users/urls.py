from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views
from .views import * #Loginform,Logout_view,register
#from .views import 
from django.conf.urls import url

urlpatterns = [
    path('Register', views.Register, name='Register'),
    path('Login', views.Loginform, name='Login'),
    path('Logout',views.Logout_view),
    path('Myorder',views.Myorder,),
    path('Newpass',views.Newpass, name = "ChangePassword"),
    path('Accountprofile',views.Accountprofile,),
    path('Address',views.Address,),
    path('UpdateProfile',views.UpdateProfile,),

    #url(r'^registration/$',views.registration),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
