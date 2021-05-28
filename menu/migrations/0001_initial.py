# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-13 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=200)),
                ('city', models.CharField(choices=[('mumbai', 'Mumbai'), ('delhi', 'Delhi'), ('kolkata', 'Kolkata'), ('bengaluru', 'Bengaluru')], max_length=100, null=True)),
                ('pin', models.BigIntegerField(max_length=8)),
                ('plan', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]