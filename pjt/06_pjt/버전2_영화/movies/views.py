from django.shortcuts import render,redirect
from .froms import CommentForm, MovieForm, MovieLikeUsersForm
from .models import Comment, MovieLikeUsers, Movie
from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.   
@require_http_methods(["GET"]) 
def index(request):
  movies = Movie.objects.all()
  context = {
    'movies' : movies,
  }
  return render(request, 'movies/index.html', context)

@login_required
@require_http_methods(["GET", "POST"]) 
def create(request):
  if request.method == "POST":
    form = MovieForm(request.POST)
    if form.is_valid():
      movie = form.save(commit=False)
      movie.user = request.user
      form.save()
      return redirect('movies:detail', movie.pk)
  elif request.method == "GET":
    form = MovieForm()
  context = {
    'form' : form,
  }
  return render(request, 'movies/create.html', context)

@login_required
@require_http_methods(["GET", "POST"]) 
def update(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  if request.method == 'POST':
    form = MovieForm(request.POST, instance=movie)
    if form.is_valid():
      form.save()
      return redirect('movies:detail', movie_pk)
  elif request.method == 'GET':
    form = MovieForm(instance=movie)
  context = {
    'form':form,
    'movie': movie,
  }
  
  return render(request, 'movies/update.html', context)
    
@require_http_methods(["GET"]) 
def detail(request, movie_pk):
  movie = Movie.objects.get(pk=movie_pk)
  comments = movie.comment_set.all()
  form = CommentForm()
  context = {
    'movie': movie,
    'comments' : comments,
    'form':form,
  }
  return render(request, 'movies/detail.html', context)

@login_required
@require_http_methods(["POST"]) 
def delete(request, movie_pk):
  return redirect('movies:index')

@login_required
@require_http_methods(["POST"])
def comment_create(request, movie_pk):
  form = CommentForm(request.POST)
  movie = Movie.objects.get(pk=movie_pk)
  user = request.user
  if form.is_valid():
    comment = form.save(commit=False)
    comment.user = user
    comment.movie = movie    
    form.save()
  return redirect('movies:detail', movie_pk)

@login_required
@require_http_methods(['POST'])
def comments_delete(request, movie_pk, comment_pk):
  comment = Comment.objects.get(pk=comment_pk)
  comment.delete()
  return redirect('movies:detail', movie_pk)

