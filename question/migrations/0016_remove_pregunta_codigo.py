# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 19:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0015_remove_pregunta_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='codigo',
        ),
    ]
