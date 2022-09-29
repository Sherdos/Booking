from django.db import models
from apps.settings.models import Currency
from apps.places.models import Places
from apps.users.models import User

# Create your models here.
class Сategories(models.Model):
    day_count = models.PositiveIntegerField(verbose_name = 'Количество дней')
    people = models.PositiveIntegerField(verbose_name = 'Количество людей')
    clas = models.CharField(max_length = 255, verbose_name = 'Класс')





class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'hotel_user', verbose_name = 'Владелец')
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'advertisement_image')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_buy',verbose_name='Название валюты')
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    city = models.ForeignKey(Places, on_delete=models.CASCADE, related_name='place_slug', verbose_name='Местоположение')
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'
