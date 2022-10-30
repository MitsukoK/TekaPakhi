from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import LogOutView, UserView

urlpatterns = [
    path("", UserView.as_view(), name="userview"),
    path("login/", obtain_auth_token, name="login"),
    path("logout/", LogOutView.as_view(), name="logout"),
]
