# Generated by Django 3.2.7 on 2021-09-11 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('cheese_type', models.CharField(max_length=100, verbose_name='Тип сыра')),
                ('dough_thickness', models.CharField(max_length=100, verbose_name='Толщина теста')),
                ('secret_ingredient', models.CharField(max_length=100, verbose_name='Секретный ингредиент')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.restaurant', verbose_name='Категория')),
            ],
        ),
    ]
