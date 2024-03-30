from django.db import models

# Create your models here.
# 게시글 정보를 저장 할 수 있는 class
# class는 django 제공 models.Model class를 상속
    # class를 상속 받으면
        # > 부모 클래스가 가진 각종 메서드, 속성 등을 
        # 직접 정의하지 않아도 똑같이 사용 가능
class Article(models.Model):
    # 필드 정의
    # title 변수는 무슨 변수?
    # 클래스 변수 > 모든 인스턴스가 공통으로 가지는 속성
    title = models.CharField(max_length=150)
    # 글자 수 제한 없는 문자열 공간
    content = models.TextField() 
    # 자동으로 현재 시간을 추가된 시점에만 기록
    created_at = models.DateTimeField(auto_now_add=True)
    # 자동으로 현재 시간을 매번 기록
    updated_at = models.DateTimeField(auto_now=True)

'''
    파이썬 (views.py) 파일에서 사용하기 편하게 
    class로 DB의 모양을 정의했고, 그 class의 instance로 값들을 다룰것
    DB에 class로 만든 데이터 schema를 실제 테이블로 만들려면 SQL로 만들어야 한다
    > django가 알아서 해준다.
    >> makemigrations 명령어를 머넞 입력 해야 했었다.
    views.py에서 쉽게 사용하기 위해 내가 정의한 Model의 기분 구조 
'''

# Article 클래스의 인스턴스를 생성한다.
# article_1 = Article()
# # 이 때의 title은 인스턴스 article_1의 속성 title
# article_1.title = '제목1'
# article_1.content = '내용1'
# article_1.save()

# article_2 = Article()
# article_2.title = 'article_1.title과 똑같은 규칙 적용'
# article_2.content = '내용2'
# article_2.save()
