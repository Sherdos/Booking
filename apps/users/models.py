from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(
        upload_to = 'profile_image/',
        verbose_name='Фотография профиля',
        blank = True, null = True,
        default = 'profile_image/no_image.png '
        )
    
    phone = models.CharField(
        max_length=100,
        verbose_name="Телефонный номер",
        blank = True, null = True
    )
    status_user = models.BooleanField(
        verbose_name = 'Статус пользователя',
        default = False
    )
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        


