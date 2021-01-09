from django.urls import path
from . import views

urlpatterns=[
    path('', views.index),
    path('authors', views.authors),
    path('see_book/<int:book_id>', views.bookinfo),
    path('see_author/<int:author_id>', views.authorinfo),
    path('add_book', views.addbook),
    path('add_author', views.addauthor),
    path('link_author/<int:book_id>', views.linkauthor),
    path('link_book/<int:author_id>', views.linkbook)
]