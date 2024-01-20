from django.urls import path
from . import views

urlpatterns = [
    # Add more URL patterns as needed
    path('about/',views.about),
    path('contact/',views.contact)
]