# Generated by Django 4.1.6 on 2023-02-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prophetv2', '0012_delete_teststockinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestStockInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tradingName', models.CharField(max_length=100)),
                ('stockCode', models.CharField(max_length=100)),
                ('lastPrice', models.FloatField(null=True)),
                ('roe', models.FloatField(null=True)),
                ('marketcap', models.FloatField(null=True)),
                ('totalRev', models.FloatField(null=True)),
                ('pe', models.FloatField(null=True)),
                ('yieldPercent', models.FloatField(null=True)),
                ('sector', models.CharField(max_length=100)),
                ('gtiScore', models.FloatField(null=True)),
                ('oneYearChange', models.FloatField(null=True)),
            ],
        ),
    ]
