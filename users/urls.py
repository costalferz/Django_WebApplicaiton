from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views
from .views import SignUpView,Loginform,registration,logout_view
#from .views import 
from django.conf.urls import url

urlpatterns = [
    path('Register', views.SignUpView.as_view(), name='Register'),
    path('Login', views.Loginform, name='Login'),
    path('logout',views.logout_view),
    url(r'^registration/$',views.registration),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
