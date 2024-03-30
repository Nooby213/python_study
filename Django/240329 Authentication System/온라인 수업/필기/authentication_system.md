# Cookie & Session
## HTTP
- HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약
- 웹에서 이루어지는 모든 데이터 교환의 기초

### HTTP 특징
- 비 연결 지향
  - 서버는 요청에 대한응답을 보낸 후 연결을 끊음
- 무상태
  - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음

## Cookie
- 서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- 클라이언트 측에서 저장되는 작은 데이터 파일이며, 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식

### 쿠키 사용 원리
1. 브라우저는 쿠키를 KEY-VALUE의 데이터 형식으로 저장
2. 저장해둔 쿠키를 동일한 서버에 재요청시 저장된 쿠키를 함께 전송
  - 쿠키는 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단 때 주로 사용됨
    - 이를 이용해 사용자의 로그인 상태를 유지할 수 있음
    - 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억 시켜주기 때문

### 쿠키 사용 목적
1. 세션 관리
  - 로그인, 아이디 자동완성, 공지 하루 안보기, 팝업 체크, 장바구니 등의 정보 관리
2. 개인화
  - 사용자 선호, 테마 등의 설정
3. 트래킹
  - 사용자 행동을 기록 및 분석

## 세션
- 서버측에서 생성되어 클라이언트와 서버 간의 상태를 유지
- 상태 정보를 저장하는 데이터 저장 방식

### 세션 작동 원리
1. 클라이언트가 로그인을 하면 서버가 SESSION 데이터를 생성 후 저장
2. 생성된 SESSION 데이터에 인증 할 수 있는 KEY(SESSION ID)를 발급
3. 발급한 SESSION ID를 클라이언트에게 응답
4. 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키(SESSION ID가 저장된)를 서버에 전달
5. 쿠키는 요청 때마다 서버에 함께 전송 되므로 서버에서 SESSION ID를 확인해 로그인 되어있다는 것을 알도록 함
- 로그아웃은 SESSION 데이터를 제거하는 것

### 쿠키 종류별 Lifetime
1. Session cookie
  - 현재 세션이 종료되면 삭제됨
  - 브라우저 종료와 함께 세션이 삭제됨
2. Persistent cookies
  - Expires 속성에 저장된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제됨

### 세션 in Django
- Django는 database-bakced sessions 저장 방식을 기본 값으로 사용
- session 정보는 DB의 django_session 테이블에 저장됨
- Django는 요청안에 특정 session id를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 session 데이터를 알아냄
---
# Autentication System

## Django Authentication System (인증 시스템)
- 사용자 인증과 관련된 기능을 모아 놓은 시스템

### Authentication
- 사용자가 자신이 누구인지 확인하는 것

### User model 대체하기
- 대체하는 이유
  - auth앱에 작성된 User 클래스를 사용했음
- 별도의 설정 없이 사용할 수 있어 간편하지만, 개발자가 **직접 수정할 수 없는** 문제가 존재
```python
# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

# settings.py
AUTH_USER_MODEL = 'accounts.User'

# accounts/models.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```
- **주의**
  - 프로젝트 중간에 AUTH_USER_MODEL을 변경 할 수 없음
  - 이미 프로젝트가 진행되고 있을 경우 데이터베이스 초기화 후 진행
  - 새 프로젝트를 시작하는 경우 커스텀 User모델을 설정하는 것을 강력하게 권장하고 있음
  - 커스텀 User 모델은 기본 User 모델과 동일하게 작동하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문
  - 단, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야함 

### Login
- Session을 create하는 과정
- AutenticationForm()
  - 로그인 인증에 사용할 데이터를 입력 받는 built-in form
  - DB에 저장되지 않는 데이터를 받는 Form
```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
# Create your views here.

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)
```

### Logout
- Session을 Delete하는 과정
- logout(request)
  - 현재 요청에 대한 Session Data를 DB에서 삭제
  - 클라이언트의 쿠키에서도 Session Id를 삭제
```python
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('accounts:login')
```

### Template with Authentication data
- 템플릿에서 인증 관련 데이터를 출력하는 방법
```python 
<h2>반갑습니다, {{  user.username  }} 님</h2>

# settings.py
'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
```