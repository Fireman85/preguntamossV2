# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-12 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_post',
            field=models.ImageField(blank=True, upload_to='pic_folder/', verbose_name='imagen adjunta'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='Url de la nota', max_length=63, unique_for_month='pub_date', verbose_name='url'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='contenido'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=63, verbose_name='titulo'),
        ),
    ]
