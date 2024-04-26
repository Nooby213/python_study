# DB 설계를 활용한 REST API 설계 - 주제 : 영화


## A. 전체 배우 목록 제공

### 어려웠던 점
- templates 안쓰고 어떻게 전체 배우 목록을 제공해야할지 고민이었습니다.
- DRF를 어떻게 설치할지 고민이었습니다.


### 해결방법
- POSTMAN를 이용하여 해결 할 수 있었습니다.
- `pip install drf-spectacular` 설치가 필요합니다.
```python
# serializers.py
# A. 전체 배우 목록 제공
class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'


# views.py
@api_view(['GET'])
def actor_list(request):
    if request.method == 'GET':
        actors = Actor.objects.all()
        serializer = ActorListSerializer(actors, many=True)
        return Response(serializer.data)
```
이때, `serializer = ActorListSerializer(actors, many=True)` 에 유의해야 합니다.
Serializer 대상이 QuerySet이기 때문에 "many=True" 가 필요합니다.


## B. 단일 배우 정보 제공(출연 영화 제목 포함)

### 어려웠던 점
- actor 클래스에는 없는 movie정보를 제공하는 것이 어려웠습니다.

### 해결법
- 영화 정보를 가져오는 시리얼라이즈를 만든다음 단일배우정보 시리얼라이즈에서 사용해주었습니다.
- ManyRelatedManager 때문에 `many=True`를 사용해야 했습니다.
```python
# 출연영화 제목
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)
# 단일 배우 정보 제공
class ActorDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ('id', 'name', 'movies')  # 필드 순서를 조정합니다.
```


## C. 전체 영화 목록 제공
### 어려운점
- 전체 배우 정보 제공이랑 같았기에 참고하였습니다.

### 해결방법
- 역시 serializer = MovieListSerializer(movies, many=True) 을 주의하며 view를 작성해 줍니다.
```python
# C. 전체 영화 정보 제공
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','overview',)



# views.py
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
```


## D. 단일 영화 목록 제공
### 어려운점
- 출연배우 이름과 리뷰 목록을 포함해야 했습니다.


### 해결방법
- B번을 이용하여 해결하였습니다.
- 출연배우와 리뷰정보를 가지고 있는 Serializer를 각각 만들었습니다.
- 이를 단일영화목록을 제공하는 Serializer에서 불러와 사용했습니다.
- 이때, many=True, read_only=True 옵션을 넣어줘야 합니다.

```python
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
```


## E. 전체 리뷰 목록 제공
### 어려운점
- A번과 비슷했습니다.
- views.py 에서 `serializer = ReviewListSerializer(reviews, many=True)` 코드를 주의해주세요.

### 해결방법
```python
# E. 전체 리뷰 목록 제공
class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title','content',)

# views.py
@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
```

## F. 단일 리뷰 조회& 수정 & 삭제

### 어려운점
- 리뷰가 작성된 영화 정보를 조회하는 것이 어려웠습니다.
- 수정과 삭제 구현이 어려웠습니다.

### 해결방법
- B 번에서 사용한 "MovieSerializer"를 사용했습니다.
- 이때, 리뷰는 한개의 영화에서 남겨지므로 `movie = MovieSerializer()` 를 사용했습니다.
- many 사용 안해도 됩니다.

- 수정
  - `serializer = ReviewDetailSerializer(review, data=request.data, partial=True)`
  - "partial=True" 를 사용하여 부분수정을 허용해 줬습니다.

- 삭제
  - 삭제되었다는 메시지를 출력하는 것이 까다롭습니다.

```python
@api_view(['GET','PUT', 'DELETE'])
def review_detail(request,review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    
    # 수정
    elif request.method == 'PUT':
        serializer = ReviewDetailSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 삭제
    elif request.method == 'DELETE':
        review.delete()
        # 삭제되었다는 메시지 출력
        data = {
            "message": f"review {review_pk} is deleted."
        }
        return Response(data)
```


## G. 리뷰 생성
### 어려운점
- 어떤 Serializer를 사용할지가 고민이었습니다.
- view함수 작성 중 특정 값(movie)이 필요하다며 정상적으로 구현이 안되었습니다.
- 작성된 리뷰를 movie에 어떻게 저장할지 고민이었습니다.

### 해결방법
- F에서 사용한 단일리뷰 Serializer를 사용하면 되었습니다.
- "partial=True"를 사용하여 값을 전부 입력하지 않아도 작동되게 하였습니다.
- save를 활용하면 저장이 가능했습니다. `serializer.save(movie=movie)`

```python
@api_view(['POST'])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = ReviewDetailSerializer(data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        # serializer.validated_data['movie'] = movie, 좀 더 정확한 코드입니다.
        serializer.save(movie=movie) # 영화에 리뷰를 저장
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```