# Model

## Django Model
- DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
- 테이블 구조를 설계하는 청사진
![DB테이블](/DB테이블.JPG)
- django.db.models 모듈의 Model이라는 부모 클래스를 상속받음
- Model은 model에 관련된 모든 코드가 이미 작성 되어있는 클래스
- 테이블 구조를 어떻게 설계할지에 대해 코드만 작성하도록 위한 것
- 필드 이름 = 필드 데이터 타입(선택 : 필드 제약 조건)

## Migrations
- model 클래스의 변경사항(필드 생성, 수정 삭제 등)을 DB에 최종 반영하는 방법
- 핵심 명령어 2가지
  - $ python manage.py makemigrations
    - model class를 기반으로 최종 설계도 작성
  - $ python manage.py migrate
    - 최종 설계도를 DB에 전달하여 반영

### 추가 모델 필드 작성
1. class에 추가사항 입력
2. 이미 기존의 테이블이 존재하기 때문에 기본 값 설정이 필요
  1. 대화를 유지하면서 직접 기본 값을 입력하는 방법(그냥 엔터치면 알아서해줌)
  2. 현재 대화에서 나간 후 models.py에 기본 값 관련 설정을 하는 방법
3. 추가하는 필드의 기본값을 입력해야하는 상황
   1. 날짜 데이터는 직접 입력하기 보다 Django가 제안하는 기본 값을 사용하는 것을 권장
   2. 아무것도 입력하기 않고 Enter를 누르면 Django가 제안하는 기본 값으로 설정 됨
4. migrations 과정 종료 후 2번째 migration 파일이 생성됨을 확인
  - 0002_어쩌구_저쩌구
  - 설계도의 문제가 생겼을 시 복구하거나 되돌릴 때 사용
5. migrate 후 테이블 필드 변화 확인
  - 해당 db.sqlite3에 들어가서 변화 확인
- 순서
  1. model class 변경
  2. makemigrations
  3. migrate

## Model field
- DB 테이블의 필드(열)을 정의하며, 해당 필드에 저장되는 데이터 타입과 제약조건을 정의
- CharField()
  - 길이 제한이 있는 문자열을 넣을 때 사용
  - 필드의 최대 길이를 결정하는 max_length는 필수 인자
- TextField()
  - 글자의 수가 많을 때 사용
- DateTimeField()
  - 날짜와 시간을 넣을 때 사용
  - auto_now(수정일)
    - 데이터가 저장될 때마다 자동으로 현재 날짜시간을 저장
  - auto_now_add(제조일)
    - 데이터가 처음 생성될 때만 자동으로 현재 날짜시간을 저장

## Admin site
- Django는 추가 설치 및 설정 없이 자동으로 관리자 인터페이스를 제공
- 데이터 확인 및 테스트 등을 진행하는데 매우 유용
1. admin 계정 생성
  - email은 선택사항이기 때문에 입력하지 않고 진행 가능
  - 비밀번호 입력 시 보안상 터미널에 출력되지 않으니 무시하고 입력 이어가기
  - $ python manage.py createsuperuser
2. DB에 생성된 admin 계정 확인 (auth_user)
3. admin에 모델 클래스 등록
  - admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능
![계정등록](/계정등록.JPG)
4. admin site 로그인 후 모델 클래스 확인
5. 데이터 생성, 수정, 삭제 테스트
6. 테이블 확인

## 데이터베이스 초기화
1. migration 파일 삭제(청사진 삭제)
  - init.py, migrations 폴더 삭제 안하도록 유의
2. db.sqlite3 파일 삭제

## 기타 명령어
- $ python manage.py showmigrations
  - migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 명령어
  - x 표시가 있으면 migrate가 완료되었음을 의미
- $ python manage.py sqlmigrate articles 0001
  - 해당 migrations 파일이 SQL 언어(DB에서 사용하는 언어)로 어떻게 번역되어 DB에 전달되는지 확인하는 명령어

### CRUD
- 소프트웨어가 가지는 기본적인 데이터 처리 기능
  - create
  - read
  - update
  - delete