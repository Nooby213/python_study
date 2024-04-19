from .models import Movie, MovieLikeUsers, Comment
from django import forms

class MovieForm(forms.ModelForm):
  class Meta:
    model = Movie
    fields = ('title', 'description', )

class MovieLikeUsersForm(forms.ModelForm):
  class Meta:
    model = MovieLikeUsers
    fields ='__all__'

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('content',)