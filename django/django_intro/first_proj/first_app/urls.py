from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    #path('test-route1/', views.first_view),
    #path('test-route2/', views.second_view),
]