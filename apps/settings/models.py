from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=255,verbose_name="Название сайта")
    description = models.TextField(verbose_name='Описание сайта')
    logo = models.ImageField(upload_to = 'logo/')
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'


class Currency(models.Model):
    name_currency = models.CharField(max_length=50, verbose_name='Название валюты')

    def __str__(self):
        return self.name_currency
    
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'