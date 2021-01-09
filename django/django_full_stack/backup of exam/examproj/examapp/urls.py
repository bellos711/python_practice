from django.urls import path
from . import views

urlpatterns=[
    #renders
    path('', views.index),
    path('wishes', views.dashboard),
    path('wishes/new', views.new_wish_page),
    path('wishes/edit/<int:wish_id>', views.edit_wish_page),
    
    #redirects
    path('register', views.register),
    path('logout', views.logout),
    path('login', views.login),
    path('addwish', views.add_wish_logic),
    path('editwish/<int:wish_id>', views.edit_wish_logic),
    path('grant/<int:wish_id>', views.grant_wish_logic),
    path('like/<int:wish_id>', views.add_like_logic)
]