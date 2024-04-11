# API
- 두 소프트웨어가 서로 통신할 수 있게 하는 메커니즘
- 클라이언트-서버처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계
- 
## WEB API
- 웹 서버 또는 웹 브로우저를 위한 API
- 현대 웹 개발은 여러 Open API들을 활용하는 추세
- 대표적인 Third Party Open API 서비스 목록
  - Youtube API
  - Google API
  - Naver Papago API
  - Kakao Map API

## REST API
- API Server를 개발하기 위한 일종의 소프트웨어 설계 "방법론"
- 자원을 정의(데이터)하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술
- REST라는 설계 디자인 약속을 지켜 구현한 API

### REST에서 자원을 사용하는 3가지 방법
1. 자원의 식별 (위치)
 - URI : Uniform Resource Locator (통합 자원 위치)
    - 인터넷에서 리소스(자원)를 식별하는 문자열
    - 가장 일반적으로 URI는 웹 주소로 알려진 URL
    - 네트워크 상에 리소스가 어디 있는지를 알려주기위한 약속
  - Schema (or Protocol)
    - 브라우저가 리소스를 요청하는데 사용해야 하는 규약
    - URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지를 나타냄
    - 기본적으로 웹은 http(s)를 요구하며 메일을 열기위한 mailto:, 파일을 전송하기 위한 ftp: 등 다른 프로토콜도 존재
  - Domain Name
    - 요청 중인 웹 서버를 나타냄
    - 어떤 웹 서버가 요구되는 지를 가리키며 직접 IP 주소를 사용하는 것도 가능하지만 Domain Name으로 사용함
  - Port
    - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문
    - HTTP 프로토콜의 표준 포트
    - HTTP - 80
    - HTTPS - 443
    - 표준 포트만 작성시 생략 가능
  - Path
    - 웹 서버의 리소스 경로
    - 초기에는 실제 파일이 위치한 물리적인 위치를 나타냈지만, 현재는 실제 위치가 아닌 추상화된 형태의 구조를 표현
    - 예를 들어 /articles/create/라는 주소가 실제 존재하지는 않음
  - Parameters
    - 웹 서버에 제공하는 추가적인 데이터
    - **&** 기호로 구분되는 key-value 쌍 목록
    - 서버는 리소스를 응답하기 전에 이러한 파라마티러르 사용하여 추가 작업을 수행할 수 있음
  - Anchor
    - 일종의 **북마크** 를 나타내며 브라우저에 해당 지점에 있는 콘텐츠를 표시
    - fragment identifiler(부분 식별자)라고 부느는 **#** 이후 부분은 서버에 전송되지 않음
    - 브라우저의 특정 위치로 이동할 수 있음

2. 자원의 행위 (행동 : CRUD)
    - HTTP Methods
      1. GET
         - 서버에 리소스의 표현을 요청
         - GET을 사용하는 요청은 데이터만 검색해야 함
      2. POST
         - 데이터를 지정된 리소스에 제출
         - 서버의 상태를 변경
      3. PUT
         - 요청한 주소의 리소스를 수정
      4. DELETE
         - 지정된 리소스를 삭제
    - HTTP response status codes
    - 특정 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타냄
      1. Informational responses (100-199)
      2. Successful responses (200-299)
      3. Redirection messages (300-399)
      4. Client error responses (400-499)
      5. Server error responses (500-599)

3. 자원의 표현 (응답 : 최종 데이터)
    - JSON 데이터
    - 궁극적으로 표현되는 데이터 결과물
    - REST API는 JSON타입으로 응답하는 것을 권장

## DRF -  Django REST framework
- Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
- INSTALLED_APP 에 추가해주어야 함
 
|---| GET | POST | PUT | DELETE |
|---|---|---|---|---|
| articles/ | 전체 글 조회 | 글 작성 |
| articles/1/ | 1번 글 조회 || 1번 글 수정 | 1번글 삭제 |


### Serialization 직렬화
- 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- 어떤 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정

```py
# apps/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)
```

### ModelSerializer
- Django 모델과 연결된 Serializer 클래스
- 일반 Serializer와 달리 사용자 입력 데이터를 받아 자동으로 모델 필드에 맞춰 Serialization을 진행

### GET

```py
# apps/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
]
```

```py
# apps/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleListSerializer

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)
```
- many 옵션
  - Serialize 대상이 QuerySet인 경우 입력
- data 속성
  - Serialize data 객체에서 실제 데이터를 추출
- **api_view** decorator
  - DRF view 함수에서는 필수로 작성되며 view 함수를 실행하기 전 HTTP 메서드를 확인
  - 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답
  - DFR view 함수가 응답해야 하는 HTTP 메서드 목록을 작성

### POST
- 게시글 데이터 생성하기
1. 데이터 생성이 성공했을 경우 201 Created 응답
2. 데이터 생성이 실패 했을 경우 400 Bad request 응답

```py
#serializers.py

from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'content',)

class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        fields = '__all__'
```
```py
# apps/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

### DELETE
```py
# apps/views.py
@api_view(['GET', 'DELETE'])
def article_detail(request, article_pk):
        article = Article.objects.get(pk=article_pk)
        if request.method == 'GET':
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        elif request.method == 'DELETE':
             article.delete()
             return Response(status=status.HTTP_204_NO_CONTENT)
```

### PUT
```py
# apps/views.py

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        # partail 부분 수정이 가능하나 필수는 아니다. False일 경우 전체 데이터 전송
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
### PATCH
- 일부 수정할때 (제한둘 수 있음)

#### raise_exception
- is_valid()의 선택인자
- 유효성 검사를 통과하지 못할 경우 ValidationError 예외를 발생시킴
- DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환

```py
elif request.method == 'POST':
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```
