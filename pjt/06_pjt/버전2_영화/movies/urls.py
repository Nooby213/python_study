from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:movie_pk>/detail/', views.detail, name='detail'),
    path('<int:movie_pk>/update/', views.update, name='update'),
    path('<int:movie_pk>/delete/', views.delete, name='delete'),
    path('<int:movie_pk>/comments_create/', views.comment_create, name='comment_create'),
    path('<int:movie_pk>/comments_delete/<int:comment_pk>', views.comments_delete, name='comments_delete'),
]
