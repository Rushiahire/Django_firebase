from os import name
from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('sign_in',views.SignIn.as_view(),name='signin'),
    path('login',views.Login.as_view(),name='login')
    
]
