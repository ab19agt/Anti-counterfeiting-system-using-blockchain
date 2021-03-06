# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-05-20 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_product2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=200)),
                ('pid', models.CharField(max_length=200)),
                ('amount', models.CharField(max_length=200)),
                ('tx', models.CharField(max_length=200)),
                ('status', models.CharField(default='pending', max_length=200)),
                ('unique_id', models.CharField(max_length=200)),
            ],
        ),
    ]
