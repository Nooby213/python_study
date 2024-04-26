from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Actor,Movie, Review
from .serializers import ActorListSerializer, ActorDetailSerializer, MovieListSerializer, MovieDetailSerializer, ReviewListSerializer, ReviewDetailSerializer
# Create your views here.
@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all()
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def actor_detail(request,actor_pk):
    actor = Actor.objects.get(pk=actor_pk)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    

@api_view(['GET','PUT', 'DELETE'])
def review_detail(request,review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewDetailSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        review.delete()
        data = {
            "message": f"review {review_pk} is deleted."
        }
        return Response(data)

@api_view(['POST'])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewDetailSerializer(data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        # serializer.validated_data['movie'] = movie
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)