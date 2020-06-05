from django.db import models
from django.urls import reverse


class Category(models.Model):

    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Machine(models.Model):

    class Transmission(models.TextChoices):
        MECHANICAL = 'механическая'

    name = models.CharField("Машина", max_length=50)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    price = models.IntegerField("Цена", null=True)
    description = models.TextField("Описание")
    image = models.ImageField("Главная фотография", upload_to="machines/")

    wheels_formula = models.CharField("Колесная формула", max_length=5)
    curb_weight = models.FloatField("Снаряженная масса", null=True)
    crew = models.PositiveSmallIntegerField("Экипаж", null=True)
    passengers = models.PositiveSmallIntegerField("Пассажиры", null=True)
    armor = models.FloatField("Толщина брони", null=True)
    engine = models.CharField("Двигатель", max_length=50)
    power = models.FloatField("Мощность", null=True)
    transmission = models.CharField("Трансмиссия",
                                    choices=Transmission.choices,
                                    default=Transmission.MECHANICAL, max_length=50)

    buses = models.CharField("Шины", null=True, max_length=50)
    suspension = models.CharField("Подвеска", null=True, max_length=50)
    length = models.PositiveSmallIntegerField("Длина", null=True)
    width = models.PositiveSmallIntegerField("Ширина", null=True)
    height = models.PositiveSmallIntegerField("Высота", null=True)
    speed = models.PositiveSmallIntegerField("Скорость", null=True)

    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('machine_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"


class CombatNutrion(models.Model):

    name = models.CharField("Боепитание", max_length=50)
    price = models.IntegerField("Цена", null=True)
    country = models.CharField("Страна производитель", max_length=50)
    description = models.TextField("Описание")
    weight = models.FloatField("Вес", null=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    image = models.ImageField("Главная фотография", upload_to="combat_nutrion/")

    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('combat_nutrion_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = "Боепитание"
        verbose_name_plural = "Боепитание"

