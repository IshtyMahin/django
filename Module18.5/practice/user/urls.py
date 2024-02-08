

from  django.urls import path 

from . import views

urlpatterns = [
    path('signup/',views.RegisterView.as_view(),name='signup'),
    path('login/',views.UserLoginView.as_view(),name ='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.ProfileView.as_view(),name ='profile'),
    path('profile/edit',views.EditProfileView.as_view(),name ='edit_profile'),
    path('profile/edit/passChange',views.PasswordChangeView.as_view(),name ='pass_change'),
    path('profile/edit/passChangeWithoutOldPassword',views.Without_Old_pass_PasswordChangeView.as_view(),name ='pass_change_without_old_password'),
     
]
