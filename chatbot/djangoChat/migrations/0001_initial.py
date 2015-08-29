# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userID', models.IntegerField()),
                ('username', models.CharField(max_length=300)),
                ('is_chat_user', models.BooleanField(default=False)),
                ('gravatar_url', models.CharField(max_length=300)),
                ('last_accessed', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('gravatar', models.CharField(max_length=300)),
            ],
        ),
    ]
