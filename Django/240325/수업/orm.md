# ORM
- Object-Relational-Mapping
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

## QuerySet API
- ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구
  - API를 사용하여 SQL이 아닌 python 코드로 데이터를 처리

### Query
- 데이터베이스에 특정한 데이터를 보여 달라는 요청
- 쿼리문을 작성한다
  - 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.
- 파이썬으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달

### QuerySet
- 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
  - 순회가 가능한 데이터로써 1개 이상의 데이터를 불어와 사용할 수 있음
- Django ORM을 통해 만들어진 자료형
- 단, 데이터베이스가 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

### QuerySet API
- python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제하는 것
-  $ pip install ipython (업그레이드 된 shell)
   -  python -i
   -  exit() 탈출
-  $ pip install django-extensions (확장팩)
   -  settings.py 의 INSTALLED_APPS = ['django_extensions']

### Django shell
- Django 환경 안에서 실행되는 python shell
- 입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미침
- $ python manage.py shell_plus
1. 
```python
In [1]: article = Article()

In [2]: article.title = 'first'

In [3]: article.content = 'django!'

In [4]: article.save()
```
2. 

```python
article = Article(title = 'second', content = 'django!')
```
3. 
```python
# 리턴 값을 가짐
Article.objects.create(title = 'third', content = 'django!')
Out: <Article: Article object (3)>
```

### Read
#### 대표적인 조회 메서드
- Return new QuerySets - 쿼리셋 조회
  - all() : 모든 데이터 조회
    - Article.objects.all() 
  - filter() : 특정 조건 데이터 조회
    - articles = Article.objects.filter(content = 'django!')
    - 없을 경우 빈 쿼리셋 리턴
- Do not return QuerySets - 단일 데이터 조회
  - get()
  - 각각의 데이터가 가지고 있는 고유한 값을 조회할 때에만 쓴다.
    - 찾을 수 없거나 둘 이상의 객체를 찾으면 예외를 발생시킴
    - primary key(pk)와 id같이 고유성을 보장하는 조회에서 사용해야 함
  - article = Article.objects.get(pk=1)

### Update
1. 조회
  - article = Article.objects.get(pk=3)
2. 수정
  - article.title = 'SSAFY'
3. 저장
  - article.save()

### Delete
1. 조회
  - article = Article.objects.get(pk=2)
2. 삭제
  - article.delete()
  - 삭제된 객체가 리턴됨 (1, {'articles.Article': 1})
  - 이미 지워진 pk값은 재사용 하지 않는다. 

### Field lookups
- 특정 레코드에 대한 조건을 설정하는 방법
- QuerySet 메서드 filter(), exclude(), 및 get()에 대한 키워드 인자로 지정
- django queryset api (참고)