# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 19:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0016_remove_pregunta_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuesta',
            name='descripcion_code',
        ),
    ]
