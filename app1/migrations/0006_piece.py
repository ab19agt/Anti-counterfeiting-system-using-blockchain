# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-06-14 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_transaction_sid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sh_id', models.CharField(max_length=200)),
                ('seller_id', models.CharField(max_length=200)),
                ('seller_name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('offer', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('unique_id', models.CharField(max_length=200)),
                ('product_id', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('about_pro', models.CharField(max_length=200)),
                ('seller_price', models.IntegerField()),
            ],
        ),
    ]
