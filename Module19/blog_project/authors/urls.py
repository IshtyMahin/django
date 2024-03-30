

from django.contrib import admin
from django.urls import path,include
from .views import register,user_login,profile,pass_change,edit_profile,user_logout
from . import views
from django.contrib.auth.views import LogoutView 
urlpatterns = [
     path('register/',register,name ='register'),
     # path('login/',user_login,name ='login'),
     path('login/',views.UserLoginView.as_view(),name ='login'),
     # path('logout/',LogoutView.as_view(),name ='logout'),
     path('logout/',user_logout,name ='logout'),
     path('profile/',profile,name ='profile'),
     path('profile/edit',edit_profile,name ='edit_profile'),
     path('profile/edit/passChange',pass_change,name ='pass_change'),
     
]
