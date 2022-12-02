from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view

urlpatterns = [
    path("dashboard/", dashboardPageView, name="dashboard"),
    path("newFood/", newFoodPageView, name="newFood"),
    path("commitFood/", commitFood, name="commitFood"),
    path("viewSerums/", viewSerums, name="viewSerums"),
    path("editSerum/", editSerum, name="editSerum"),
    path("editPerson/", editPerson, name="editPerson"),
    path("editJournal/", editJournal, name="editJournal"),
    path("commitPerson/", commitPerson, name="commitPerson"),
    path("commitJournal/", commitJournal, name="commitJournal"),
    path("delPerson/", delPerson, name="delPerson"),
    path("delJournal/", delJournal, name="delJournal"),
    path("commitSerum/", commitSerum, name="commitSerum"),
    path("delSerum/", delSerum, name="delSerum"),
    path("viewPeople/", viewPeople, name="viewPeople"),
    path("searchFood/", searchFoodPageView, name="searchFood"),
    path("login/", auth_view.LoginView.as_view(template_name='healthtracker/login.html'), name="login"),
    path("accountregister/", accountRegisterView, name="account"),
    path("logout/", auth_view.LogoutView.as_view(template_name='healthtracker/logout.html'), name="logout"),
    path("profile/", profilePageView, name="profile"),
    path("submituser/", submituser, name="submituser"),
    path("submitmeal/", submitmeal, name="submitmeal"),
    path("", indexPageView, name="index"), 
]    