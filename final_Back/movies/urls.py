from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'movies'

urlpatterns = [
    path('getMovieList/',views.movie_data_extract),
]