from django.db import models
# #함수 형식으로 경로 설정
# def articles_image_path(instance, filename):
#     return f'image/{instance.user.username}/{filename}'
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='%y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
