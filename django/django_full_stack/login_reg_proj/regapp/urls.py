from django.urls import path
from . import views

urlpatterns=[
    #renders
    path('', views.index),
    path('dashboard', views.dashboard),
    
    #redirects
    path('register', views.register),
    path('logout', views.logout),
    path('login', views.login)
]