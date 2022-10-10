from django.db import models
from apps.countries.models import Nation

# Create your models here.

# City

class Places(models.Model):

    title = models.CharField(
        max_length = 255,
        verbose_name = 'Название места'
        )

    slug = models.SlugField(
        verbose_name='Слаг места'
        )

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f' {self.title}'

# Places_for_rest

class Places_for_rest(models.Model):

    nation = models.ForeignKey(
        Nation, on_delete=models.CASCADE,
        related_name='nation',
        verbose_name='Страна'
        )
   
    image_rest = models.ImageField(
        upload_to = 'advertisement_image'
        )

    slug = models.ForeignKey(
        Places, on_delete=models.CASCADE,
        related_name = 'slug_place',
        verbose_name='Название места'
        )

    class Meta:
        verbose_name = 'Места для отдыха'
        verbose_name_plural = 'Места для отдыха'

    def __str__(self):
        return f'{self.slug}, {self.nation}'
