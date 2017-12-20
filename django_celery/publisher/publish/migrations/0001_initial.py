# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-20 15:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created Date')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
