from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Genre, Movie
import random
from django.http import JsonResponse


# Create your views here.
@require_safe
def index(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        genres = Genre.objects.all()
        
        context = {
            'movies':movies,
            'genres':genres
        }

        return render(request, 'movies/index.html', context)


def filter_genre(request):
    if request.method == 'GET':
        genre = request.GET.get('genre')
        if genre:
            movies = Movie.objects.filter(genres__name=genre)
        else:
            movies = Movie.objects.all()

        movie_data = [{'title': movie.title} for movie in movies]
        return JsonResponse({'movies': movie_data})

@require_safe
def recommended(request):
    genres = Genre.objects.all()
<<<<<<< HEAD
    
    # 장르 중에서 랜덤으로 하나 선택
    random_genre = random.choice(genres)
    
    # 선택된 장르에 속하는 영화 중에서 랜덤으로 5개 선택
    recommended_movies = random_genre.movie_set.all().order_by('?')[:5]
    context = {
        'movies': recommended_movies
        }
    
    return render(request, 'movies/recommended.html', context)
'''
랜덤으로 장르를 고르고 해당 장르의 영화를 출력


'''
=======
    movies = Movie.objects.all()

    if request.method =='GET':
        seleced_genre_id = request.GET.get('genre_id')

        if seleced_genre_id:
            selected_genre = Genre.objects.get(pk=seleced_genre_id)
            recommended_movies = movies.filter(genres=selected_genre)
        
        else:
            recommended_movies = movies
    
    context = {
        'genres':genres,
        'movies':movies,
    }
    
    return render(request,'movies/recommended.html', context)
>>>>>>> lsm
