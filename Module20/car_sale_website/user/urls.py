

from  django.urls import path 

from . import views

urlpatterns = [
    path('signup/',views.RegisterView.as_view(),name='signup'),
    path('login/',views.UserLoginView.as_view(),name ='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.ProfileView.as_view(),name ='profile'),
    path('profile/edit',views.EditProfileView.as_view(),name ='edit_profile'),
    path('profile/edit/passChange',views.PasswordChangeView.as_view(),name ='pass_change'),
    path('buy/<int:id>',views.buy_car,name='buy_car'),
    path('profile/delete_purchase/<int:purchase_id>/', views.delete_purchase, name='delete_purchase'),
     
]
