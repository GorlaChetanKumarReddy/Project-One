"""Project0101 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cusers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cusers_register/',views.cusers_register,name='cusers_register'),
    path('cusers_register_request/',views.cusers_register_request,name='cusers_register_request'),
    path('cuser_log_in/',views.cuser_log_in,name='cuser_log_in'),
    path('cuser_loin_request/',views.cuser_loin_request,name='cuser_loin_request'),
]
