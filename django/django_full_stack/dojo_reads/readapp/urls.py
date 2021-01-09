from django.urls import path
from . import views

urlpatterns=[
    #renders
    path('', views.index),
    path('books', views.dashboard),
    path('add', views.add_book_page),
    path('books/<int:book_id>', views.bookinfo),
    
    
    #redirects
    path('register', views.register),
    path('logout', views.logout),
    path('login', views.login),
    path('add_author', views.add_author_logic),
    path('addbook', views.addbook_logic)
]