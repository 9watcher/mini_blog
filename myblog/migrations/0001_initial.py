# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='\u535a\u6587\u7f16\u53f7')),
                ('title', models.CharField(max_length=256, verbose_name='\u6807\u9898')),
                ('content', models.CharField(db_index=True, max_length=256, verbose_name='\u5185\u5bb9')),
                ('type', models.CharField(max_length=256, verbose_name='\u7c7b\u578b')),
                ('published_time', models.DateTimeField(verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('update_time', models.DateTimeField(verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
        ),
    ]