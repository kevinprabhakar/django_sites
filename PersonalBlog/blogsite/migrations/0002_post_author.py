# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 01:53
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=django.contrib.auth.models.User, max_length=50),
        ),
    ]
