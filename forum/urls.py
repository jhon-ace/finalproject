from django.urls import path

from . import views

urlpatterns = [
    path('',views.LoginPage, name='login-page'),
    path('dashboard',views.Dashboard, name='dashboard')

]