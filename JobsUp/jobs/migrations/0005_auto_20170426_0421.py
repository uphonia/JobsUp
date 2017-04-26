# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20170425_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='jobs.Profile')),
                ('username', models.CharField(max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('hashid', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='jobs.Profile')),
                ('username', models.CharField(max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('hashid', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='hashid',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='personnel',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='username',
        ),
        migrations.AddField(
            model_name='profile',
            name='degree',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.User'),
        ),
        migrations.AddField(
            model_name='application',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Company'),
        ),
    ]
