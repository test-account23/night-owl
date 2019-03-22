# Generated by Django 2.1.7 on 2019-03-22 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_auto_20190321_2120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nc1products',
            options={'verbose_name_plural': 'Menu items of Block 3 Night Canteen'},
        ),
        migrations.AlterModelOptions(
            name='nc2products',
            options={'verbose_name_plural': 'Menu items of Block 7 Night Canteen'},
        ),
        migrations.AlterModelOptions(
            name='nc3products',
            options={'verbose_name_plural': "Menu items of Girl's Block Night Canteen"},
        ),
        migrations.AlterModelOptions(
            name='paidordersnc1',
            options={'verbose_name_plural': 'List of orders created - Block 3 Night Canteen'},
        ),
        migrations.AlterModelOptions(
            name='paidordersnc2',
            options={'verbose_name_plural': 'List of orders created - Block 7 Night Canteen'},
        ),
        migrations.AlterModelOptions(
            name='paidordersnc3',
            options={'verbose_name_plural': "List of orders created - Girl's Block Night Canteen"},
        ),
    ]
