from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'movies'

urlpatterns = [
    #path('getMovieList/',views.movie_data_extract),
    path('',views.movie_list),
    path('ostQuiz/',views.ostQuiz),
    path('recommend/',views.recommend),
    path('/<int:movie_pk>/',views.movie_detail),
]