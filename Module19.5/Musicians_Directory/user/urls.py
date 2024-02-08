

from  django.urls import path 

from . import views

urlpatterns = [
    path('signup/',views.RegisterView.as_view(),name='signup'),
    path('login/',views.UserLoginView.as_view(),name ='login'),
    path('logout/',views.user_logout,name='logout'),
   
     
]
