# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-07-22 17:55
from __future__ import unicode_literals

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20180722_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='deepURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Url', models.CharField(max_length=254, validators=[shortener.validators.validate_Url, shortener.validators.validate_dot_com])),
                ('shortcode', models.CharField(blank=True, max_length=15, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='KirrURL',
        ),
    ]