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
from app0101 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='main'),
    path('admin_log_in/',views.admin_log_in,name='admin_log_in'),
    path('shedule_new_classes/',views.shedule_new_classes,name='shedule_new_classes'),
    path('new_shedule_classes_added/',views.new_shedule_classes_added,name='new_shedule_classes_added'),
    path('view_all_shedule_classes/',views.view_all_shedule_classes,name='view_all_shedule_classes'),
    path('update_shedule_classes/',views.update_shedule_classes,name='update_shedule_classes'),
    path('update_shedule_classes_sucess/',views.update_shedule_classes_successf,name='update_shedule_classes_sucess'),
    path('Delete_Shedule_class/',views.Delete_Shedule_class,name='Delete_Shedule_class'),
    path('view_all_shedule_classes_Enduser/',views.view_all_shedule_classes_Enduser,name='view_all_shedule_classes_Enduser'),
    path('register_user/',views.register_user,name='register_user'),
    path('regiser_user_success/',views.regiser_user_success,name='regiser_user_success'),
    path('view_all_registerd_users/',views.view_all_registerd_users,name='view_all_registerd_users'),
    path('user_search/',views.user_search,name='user_search'),
    path('search_users/',views.search_users,name='search_users'),
    path('delete_user/',views.delete_user,name='delete_user'),
    path('user_log_in/',views.user_log_in,name='user_log_in'),
]
