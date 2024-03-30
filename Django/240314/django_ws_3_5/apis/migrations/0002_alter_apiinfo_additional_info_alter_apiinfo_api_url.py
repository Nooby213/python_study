# Generated by Django 4.2.11 on 2024-03-14 07:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiinfo',
            name='additional_info',
            field=models.JSONField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='apiinfo',
            name='api_url',
            field=models.URLField(max_length=60, validators=[django.core.validators.MinLengthValidator(15, message=None), django.core.validators.URLValidator]),
        ),
    ]
