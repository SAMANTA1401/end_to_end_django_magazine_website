from django.urls import path
from authapp import views
from django.views.generic import TemplateView 
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("logout",views.handleLogout,name="handleLogout"),
    
]


