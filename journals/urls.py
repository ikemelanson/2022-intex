from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("register/", registerPageView, name="register"),
    path("dashboard/", dashboardPageView, name="dashboard"),
    path("login/", auth_view.LoginView.as_view(template_name='healthtracker/login.html'), name="login"),
    path("accountregister/", accountRegisterView, name="account"),
    path("logout/", auth_view.LogoutView.as_view(template_name='healthtracker/logout.html'), name="logout"),
    path("profile/", profilePageView, name="profile"),
    path("", indexPageView, name="index"), 
]    