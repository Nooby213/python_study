# Static Files
- 정적 파일
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일
- 이미지, JS, CSS 파일 등

## 웹 서버와 정적 파일
- 웹 서버의 기본동작은 특정위치에 있는 자원을 요청 받아서 응답을 처리하고 제공하는 것
- 이는 자원에 접근 가능한 주소가 있다라는 의미
- 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공함
- 정적 파일을 제공하기 위한 경로가 있어야 함

## Static files 제공하기
1. 기본 경로에서 제공하기
  - Static files 기본 경로 : app폴더/static/
   - {% load static %} : load태그는 상속 안된다.
  - STATIC_URL
    - 기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL
    - URL/static_URL/정적파일 경로
    - http://127.0.0.1:8000   /static   /articles/sample-1.png
    - 실제 파일이나 디렉토리가 아니며, URL로만 존재

2. 추가 경로에서 제공하기
  - STATICFILES_DIRS에 문자열 값으로 추가 경로 설정
![추가경로](/추가경로.JPG)
  - http://127.0.0.1:8000      /static/sample-2.png

# Media Files
- 사용자가 웹에서 업로드하는 정적 파일
- user-uploaded

## 이미지 업로드
- ImageField() : CharFiled()가 부모클래스, 문자열입력
- 이미지 업로드에 사용하는 모델 필드
- 이미지 객체가 직접 저장되는 것이 아닌 이미지 파일의 경로가 문자열로 DB에 저장
---
### 사전 준비
1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
```python
# settings.py
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'
```

2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 url 지정
```python
# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- $ pip install pillow
- $ python manage.py makemigrations
- $ python manage.py migrate
- pip freeze > requirements.txt
![미디어관리](/미디어경로.JPG)