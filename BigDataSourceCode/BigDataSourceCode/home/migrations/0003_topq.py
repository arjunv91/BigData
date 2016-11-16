# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-08 04:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_poststats_userstats'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewcount', models.IntegerField()),
                ('question_id', models.IntegerField()),
                ('title', models.CharField(max_length=500)),
                ('tag1', models.CharField(blank=True, max_length=100, null=True)),
                ('tag2', models.CharField(blank=True, max_length=100, null=True)),
                ('tag3', models.CharField(blank=True, max_length=100, null=True)),
                ('tag4', models.CharField(blank=True, max_length=100, null=True)),
                ('tag5', models.CharField(blank=True, max_length=100, null=True)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Tag')),
            ],
        ),
    ]