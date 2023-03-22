from django.urls import path

from book_store.views import *

urlpatterns = [
    path('', index, name='home_index'),
    path('list/', book_catalog, name='book_list'),
    path('book/<int:book_id>', book_description, name='book_description'),


]
