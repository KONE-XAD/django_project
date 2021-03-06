# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-07-22 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bookmanager', '0002_bookinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=32)),
                ('books', models.ManyToManyField(to='bookmanager.Bookinfo')),
            ],
        ),
    ]
