# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-24 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]