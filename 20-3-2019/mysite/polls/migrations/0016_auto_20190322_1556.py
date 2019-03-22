# Generated by Django 2.1.7 on 2019-03-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_auto_20190322_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paidordersnc1',
            name='filters',
            field=models.CharField(choices=[('a', 'Pending'), ('b', 'Delivered'), ('c', 'Rejected')], default='Pending', max_length=1),
        ),
        migrations.AlterField(
            model_name='paidordersnc2',
            name='filters',
            field=models.CharField(choices=[('a', 'Pending'), ('b', 'Delivered'), ('c', 'Rejected')], default='Pending', max_length=1),
        ),
        migrations.AlterField(
            model_name='paidordersnc3',
            name='filters',
            field=models.CharField(choices=[('a', 'Pending'), ('b', 'Delivered'), ('c', 'Rejected')], default='Pending', max_length=1),
        ),
    ]
