# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.AlterField(
            model_name='book',
            name='No_of_Copies',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='No_of_Requests',
            field=models.IntegerField(),
        ),
    ]