# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-28 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bbs', '0004_userprofile_friends'),
    ]

    operations = [
        migrations.CreateModel(
            name='QQGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('brief', models.TextField(default=b'nothing...', max_length=1024)),
                ('members_limit', models.IntegerField(default=200)),
                ('admin', models.ManyToManyField(related_name='group_admin', to='bbs.UserProfile')),
                ('founder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.UserProfile')),
                ('members', models.ManyToManyField(related_name='group_numbers', to='bbs.UserProfile')),
            ],
        ),
    ]
