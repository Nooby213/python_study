from rest_framework import serializers
from .models import Actor,Movie, Review

# A. 전체 배우 목록 제공
class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


# B. 단일 배우 정보 제공(출연 영화 제목 포함)
# 출연영화 제목
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)

class ActorDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies')  # 필드 순서를 조정합니다.


# C. 전체 영화 정보 제공
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','overview',)


# D. 단일 영화 정보 제공(출연 배우 이름과 리뷰 목록 포함)
# 출연 배우 이름
class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name',)


# 리뷰 목록
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('title','content',)

# 정보 제공
class MovieDetailSerializer(serializers.ModelSerializer):

    actors = ActorSerializer(many=True, read_only=True)
    reviews_set = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'actors','reviews_set', 'title', 'overview', 'release_date', 'poster_path')  # 필드 순서를 조정합니다.


# E. 전체 리뷰 목록 제공
class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title','content',)

# F. 단일 리뷰 조회
# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = ('title',)

class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()  # 단일 객체이므로 SerializerMethodField 대신 직렬화 클래스 사용

    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content')
        read_only_fields = ('movie',)


