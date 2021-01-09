from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('guess-process', views.guess_method)
]
