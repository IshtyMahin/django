

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('car/edit/<int:id>',views.edit_car,name='edit_car'),
    path('car/delete/<int:id>',views.delete_car,name ='delete_car'),
    path('car/add',views.add_car,name='add_car'),
    path('brand/add',views.add_brand,name='add_brand'),
    path('details/<int:pk>',views.DetailPostView.as_view(),name='detail_car')
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)