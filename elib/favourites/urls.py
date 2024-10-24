from django.urls import path
from .views import favourites

app_name = 'favourites'

urlpatterns = [
    path('', favourites, name='favourites'),
]