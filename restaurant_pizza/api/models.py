from django.db import models


class Restaurant(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    address = models.CharField(max_length=250, verbose_name='Адрес')

    def __str__(self):
        return self.title


class Pizza(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    cheese_type = models.CharField(max_length=100, verbose_name='Тип сыра')
    dough_thickness = models.CharField(max_length=100, verbose_name='Толщина теста')
    secret_ingredient = models.CharField(max_length=100, verbose_name='Секретный ингредиент')

    restaurant = models.ForeignKey(Restaurant, verbose_name='Ресторан', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title



