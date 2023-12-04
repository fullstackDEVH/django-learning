from django.urls import path
from . import views
from .views import UserRegisterView, UserLoginView
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('register', UserRegisterView.as_view(), name='register'),
    path('login', UserLoginView.as_view(), name='login'),
]
