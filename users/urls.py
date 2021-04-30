from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views
from .views import SignUpView
#from .views import 
urlpatterns = [
    path('Register', views.SignUpView.as_view(), name='Register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
