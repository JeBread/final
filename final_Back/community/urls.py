from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_article, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/comments/create/', views.create_comment, name='create_comment'),
    path('<int:article_pk>/like/', views.like, name='like'),
    path('<int:article_pk>/delete/',views.article_delete),
    path('comments/<int:comment_pk>/delete/',views.comment_delete),
]
