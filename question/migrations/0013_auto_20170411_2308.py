# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 04:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0012_auto_20170404_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='codigo',
            field=models.TextField(blank=True, max_length=700),
        ),
    ]
