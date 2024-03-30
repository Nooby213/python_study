from django.contrib import admin
from .models import Article
# Register your models here.

# 관리자 페이지에서
# 내가 만든 models.py에 있는 class
# 관리 할 수 있도록 등록
# Register your models here.
# 관리자 사이트에 등록
# 아싸리
admin.site.register(Article)