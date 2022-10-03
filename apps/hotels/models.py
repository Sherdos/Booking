from tabnanny import verbose
from django.db import models
from apps.settings.models import Currency
from apps.places.models import Places
from apps.users.models import User

# Create your models here.
class People(models.Model):
    people = models.CharField( max_length = 255, verbose_name = 'Тип бронирование')

    def __str__(self):
        return self.people
    
    class Meta:
        verbose_name = 'Тип бронирование'
        verbose_name_plural = 'Тип бронирование'



class Class(models.Model):
    clas = models.CharField( max_length=255, verbose_name = 'Класс номера')
    
    def __str__(self):
        return self.clas
    
    class Meta:
        verbose_name = 'Класс номера'
        verbose_name_plural = 'Класс номеров'




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


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_booking', verbose_name = 'Заказшик')
    clas = models.ForeignKey(Class, on_delete = models.CASCADE, related_name = 'class_hotel', verbose_name = 'Класс')
    people = models.ForeignKey(People, on_delete = models.CASCADE, related_name = 'people_hotel', verbose_name = 'Количество людей')
    date1 = models.CharField(max_length = 255, verbose_name = 'дата отправки')
    date2 = models.CharField(max_length = 255, verbose_name = 'дата отезда')
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, related_name = 'hotel_booking', verbose_name = 'Отель')
    def __str__(self):
        return f'{self.hotel}'
    class Meta:
        verbose_name = 'Забронированый отель'
        verbose_name_plural = 'Забронированые отели'


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_comment', verbose_name = 'Ползователь')
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, related_name = 'hotel_comment', verbose_name = 'отель' )
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(verbose_name = 'Коментарии')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Коментарии'
        verbose_name_plural = 'Коментарии'

