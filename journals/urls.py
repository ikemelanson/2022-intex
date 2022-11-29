from django.urls import path
from .views import indexPageView, registerPageView

urlpatterns = [
    path("", indexPageView, name="index"), 
    path("register/", registerPageView, name="register")  
]    