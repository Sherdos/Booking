from django.db import models
from apps.settings.models import Currency
from apps.places.models import Places

# Create your models here.
class Hotel(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = 'advertisement_image')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency_buy',verbose_name='Название валюты')
    price = models.PositiveBigIntegerField(verbose_name='Цена')
    slug = models.ForeignKey(Places, on_delete=models.CASCADE, related_name='place_slug', verbose_name='Местоположение')
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отели'