# Generated by Django 3.0.6 on 2020-05-06 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Машина')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='machines/', verbose_name='Главная фотография')),
                ('wheels_formula', models.CharField(max_length=5, verbose_name='Колесная формула')),
                ('curb_weight', models.FloatField(null=True)),
                ('crew', models.PositiveSmallIntegerField(null=True)),
                ('passengers', models.PositiveSmallIntegerField(null=True)),
                ('armor', models.FloatField(null=True)),
                ('engine', models.CharField(max_length=50, verbose_name='Двигатель')),
                ('power', models.FloatField(null=True)),
                ('transmission', models.CharField(choices=[('механическая', 'Mechanical')], default='механическая', max_length=50, verbose_name='Трансмиссия')),
                ('buses', models.CharField(max_length=50, null=True, verbose_name='Шины')),
                ('suspension', models.CharField(max_length=50, null=True, verbose_name='Подвеска')),
                ('length', models.PositiveSmallIntegerField(null=True)),
                ('width', models.PositiveSmallIntegerField(null=True)),
                ('height', models.PositiveSmallIntegerField(null=True)),
                ('speed', models.PositiveSmallIntegerField(null=True)),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Category')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.CreateModel(
            name='CombatNutrion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Боепитание')),
                ('country', models.CharField(max_length=50, verbose_name='Страна производитель')),
                ('description', models.TextField(verbose_name='Описание')),
                ('weight', models.PositiveSmallIntegerField(null=True)),
                ('image', models.ImageField(upload_to='combat_nutrion/', verbose_name='Главная фотография')),
                ('url', models.SlugField(max_length=160, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Category')),
            ],
            options={
                'verbose_name': 'Боепитание',
            },
        ),
    ]
