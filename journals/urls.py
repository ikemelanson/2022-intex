from django.urls import path
from .views import *

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("register/", registerPageView, name="register"),
    path("dashboard/", dashboardPageView, name="dashboard")
]    