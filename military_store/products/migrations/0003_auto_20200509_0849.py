# Generated by Django 3.0.6 on 2020-05-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200509_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='combatnutrion',
            name='price',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='machine',
            name='price',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Цена'),
        ),
    ]
