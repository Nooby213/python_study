from django.db import models
from django.core.validators import URLValidator
from django.core.validators import MinLengthValidator


def validate_url_min_length(value):
    min_length = 15
    if len(value) < min_length:
       return ValueError

class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    api_url = models.URLField(max_length=60, validators=[MinLengthValidator(15, message=None), URLValidator])
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.JSONField(default=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
