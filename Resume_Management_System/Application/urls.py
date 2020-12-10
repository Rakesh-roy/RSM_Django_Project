
from django.contrib import admin
from django.urls import path, include

from Application import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('register/Otp_Page/', views.otp_page, name='otp_page'),
    path('register/Otp_Page/check_otp/', views.check_otp, name='check_otp'),
]
