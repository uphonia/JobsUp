# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 18:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='hashid',
            field=models.CharField(max_length=50, null=True),
        ),
    ]