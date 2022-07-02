from django.urls import path

from webapp.views import index_view, create_guest, update_guest, delete_guest

urlpatterns = [
    path('', index_view, name="index"),
    path('guest/add/', create_guest, name="create_guest"),
    path('guest/<int:pk>/update', update_guest, name="update_guest"),
    path('guest/<int:pk>/delete', delete_guest, name="delete_guest"),
]