from django.contrib import admin
from .models import Movie, MovieLikeUsers, Comment
# Register your models here.
admin.site.register(MovieLikeUsers)
admin.site.register(Movie)
admin.site.register(Comment)