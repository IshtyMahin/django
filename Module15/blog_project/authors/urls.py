

from django.contrib import admin
from django.urls import path,include
from .views import add_author
urlpatterns = [
     path('add/',add_author,name ='add_author'),
     
]
