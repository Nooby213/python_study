# Web application (web service) 개발
- 인터넷을 통해 사용자에게 제공되는 소프트웨어 프로그램을 구축하는 과정
- 다양한 디바이스(모바일, 태블릿, PC 등)에서 웹 브라우저를 통해 접근하고 사용할 수 있음
# Client Server
- 웹의 동작 방식
![cli_ser](/클라이언트서버.JPG)
- Client
  - 서비스를 요청하는 주체 (웹 사용자의 인터넷이 연결된 장치, 웹 브라우저)
- Server
  - 클라이언트의 요청에 응답하는 주체 (웹 페이지, 앱을 저장하는 컴퓨터)
# Web Framework
- 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
- 개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공
## django
- Python 기반의 대표적인 웹 프레임워크
### django의 장점
- 다양성
  - Python 기반으로 소셜 미디어 및 빅데이터 관리 등 광범위한 서비스 개발에 적합
- 확장성
  - 대량의 데이터에 대해 빠르고 유연하게 확장할 수 있는 기능을 제공
- 보안
  - 취약점으로부터 보호하는 보안 기능이 기본적으로 내장되어 있음
- 커뮤니티 지원
  - 개발자를 위한 지원, 문서 및 업데이트를 제공하는 활성화 된 커뮤니티
  - 
### 가상환경 venv 생성
- 생성
  - $ python -m venv venv
- 동작
  - $ source venv/Scripts/activate
- 의존성 패키지 목록 생성
  - $ pip freeze > requirements.txt
- Django 프로젝트 생성
  - $ django-admin startproject firstpjt(프로젝트 이름) . 
- Django 서버 실행
  - $ python manage.py runserver
- requirements.txt 다운로드
  - pip install requirements.txt
### Django 프로젝트 생성 루틴
1. 가상 환경 생성
2. 가상 환경 활성화
3. Django 설치 (pip install django)
4. 의존성 파일 생성 (패치지 설치시마다 진행)
5. .gitignore 파일 생성 (첫 add 전)
6. git 저장소 생성
7. Django 프로젝트 생성

### 앱 생성
1. 앱 생성 (앱의 이름은 복수형으로 지정하는 것을 권장)
  - $ python manage.py startapp articles(앱의 이름)
2. 앱 등록 (반드시 앱을 생성한 후에 등록해야 함)
  - 프로젝트파일 > settings.py > INSTALLED_APPS[상단에 추가]

### 프로젝트 구조
- settings.py
  - 프로젝트의 모든 설정을 관리
- urls.py
  - 요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결
- \_\_init__.py
  - 해당 폴더를 패키지로 인식하도록 설정하는 파일
- asgi.py
  - 비동기식 웹 서버와의 연결 관리
- wsgi.py
  - 웹 서버와의 연결 관리 설정
- manage.py
  - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티

### 앱 구조
- admin.py
  - 관리자용 페이지 설정
- models.py
  - DB와 관련된 Model을 정의
  - MTV 패턴의 M
- views.py
  - HTTP 요청을 처리하고 해당 요청에 대해 응답을 봔환(url, model, template과 연계)
  - MTV 패턴의 V
- apps.py
  - 앱의 정보가 작성된 곳
- tests.py
  - 프로젝트 테스트 코드를 작성하는 곳