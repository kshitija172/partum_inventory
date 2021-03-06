# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-18 11:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pis_com', '0005_merge_20180510_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ledger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('description', models.CharField(max_length=200)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_ledger', to='pis_com.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentLedger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=65, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_ledger_payment', to='pis_com.Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
