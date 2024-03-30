from django.urls import path
from . import views
urlpatterns = [
    path("",views.set_session),
    # path("",views.get_cookie),
    # path("get/",views.get_cookie),
    path("get/",views.get_session),
    # path("del/",views.delete_cookie)
    path("del/",views.del_session)
]
