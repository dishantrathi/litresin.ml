# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-02-09 05:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_auto_20180209_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='litresinurl',
            name='shortcode',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]
