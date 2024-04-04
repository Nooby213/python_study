from django.db import models
from django.conf import settings
# django에서는 User 모델을 '직접' 참조하지 않는다.
# get_user_model() :  객체 반환, models.py 가 아닌 위치
# settings.AUTH_USER_MODEL : 문자열 반환, models.py에서만
# User모델의 이름이 바뀌거나 모델이 바뀔 수 있기때문에 직접 사용하지 않는다.
# from accounts.models import User

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
