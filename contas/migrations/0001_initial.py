# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-03 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='conta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descricao', models.CharField(blank=True, max_length=200, null=True)),
                ('estado', models.CharField(choices=[('1', 'Em Aberto'), ('2', 'Paga')], max_length=1)),
            ],
        ),
    ]