# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 22:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sound',
            name='title',
            field=models.CharField(default='title', max_length=32),
            preserve_default=False,
        ),
    ]
