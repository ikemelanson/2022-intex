from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("dashboard/", dashboardPageView, name="dashboard"),
    path("newFood/", newFoodPageView, name="newFood"),
    path("commitFood/", commitFood, name="commitFood"),
    path("viewSerums/", viewSerums, name="viewSerums"),
    path("editSerum/", editSerum, name="editSerum"),
    path("searchFood/", searchFoodPageView, name="searchFood"),
    path("login/", auth_view.LoginView.as_view(template_name='healthtracker/login.html'), name="login"),
    path("accountregister/", accountRegisterView, name="account"),
    path("logout/", auth_view.LogoutView.as_view(template_name='healthtracker/logout.html'), name="logout"),
    path("profile/", profilePageView, name="profile"),
    path("submituser/", submituser, name="submituser"),
    path("submitmeal/", submitmeal, name="submitmeal"),
    path("", indexPageView, name="index"), 
]    