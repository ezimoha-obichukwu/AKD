from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name="home"),
    path("register/", views.registration_page, name="register"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout, name="logout"),
]