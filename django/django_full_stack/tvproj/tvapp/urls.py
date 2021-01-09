from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.showslist),
    path('shows/new', views.new_show),
    path('shows/add_show', views.add_show),
    path('shows/<int:specific_show_id>', views.show_info),
    path('shows/<int:specific_show_id>/edit', views.edit_show),
    path('shows/<int:specific_show_id>/edit_show', views.edit_logic),
    path('shows/<int:specific_show_id>/delete', views.delete_logic)
]