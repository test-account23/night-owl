# Generated by Django 2.1.7 on 2019-03-20 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20190320_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paidordersnc1',
            name='block',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='paidordersnc2',
            name='block',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='paidordersnc3',
            name='block',
            field=models.CharField(max_length=10),
        ),
    ]
