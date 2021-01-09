from django.urls import path
from . import views

urlpatterns = [
    #renders
    path('', views.index),
    path('books', views.dashboard),
    path('books/<int:book_id>', views.view_edit_book),
    
    #redirects
    path('register', views.register),
    path('logout', views.logout),
    path('login', views.login),
    path('addbook', views.addbook_logic),
    path('addfavorite/<int:book_id>', views.add_fav_logic),
    path('unfavorite/<int:book_id>', views.unfav_logic),
    path('deletebook/<int:book_id>', views.delete_book_logic),
    path('editbook/<int:book_id>', views.edit_book_logic)
]