# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-02 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
        ('cliente', '0001_initial'),
        ('servico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ordens',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[('1', 'Orcamento'), ('2', 'Executando'), ('3', 'Finalizada')], max_length=1)),
                ('data_abertura', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_fechamento', models.DateTimeField(blank=True, null=True)),
                ('desc', models.CharField(blank=True, max_length=100, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cliente_ordem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='produto_item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField(default='1')),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('prod_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
        migrations.CreateModel(
            name='servico_item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade', models.IntegerField(default='1')),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('serv_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servico.servico')),
            ],
        ),
        migrations.AddField(
            model_name='ordens',
            name='prod_item',
            field=models.ManyToManyField(to='ordem.produto_item'),
        ),
        migrations.AddField(
            model_name='ordens',
            name='serv_item',
            field=models.ManyToManyField(to='ordem.servico_item'),
        ),
    ]
