from django.urls import path
from .views import search_books

app_name = 'books'

urlpatterns = [
    path('', search_books, name='search_books'),
]
