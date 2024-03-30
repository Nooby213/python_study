from django.db import models

# Create your models here.
class Diary(models.Model):
    content = models.CharField(max_length=125)
    picture = models.ImageField(blank=True, upload_to='%y/%m/%d')
    created_at = models.DateTimeField(auto_now_add=True)