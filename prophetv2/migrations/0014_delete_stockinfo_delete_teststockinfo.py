# Generated by Django 4.1.6 on 2023-02-15 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prophetv2', '0013_teststockinfo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StockInfo',
        ),
        migrations.DeleteModel(
            name='TestStockInfo',
        ),
    ]