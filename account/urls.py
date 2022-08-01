from django.urls import path
from . import views

app_name = "account"
urlpatterns = [
    path("register/", views.accountRegister, name="register"),
    path("login/", views.accountLogin, name="login"),
    path("logout/", views.accountLogout, name="logout"),
    path("profile/<str:pk>/", views.accountProfile, name="profile"),
    path("", views.index, name="index"),
]
