# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-02 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordem', '0002_servico_item_func'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordens',
            name='estado',
            field=models.CharField(choices=[(b'1', b'Em Aberto'), (b'2', b'Finalizada')], max_length=1),
        ),
    ]