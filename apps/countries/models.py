from django.db import models

# Create your models here.
class Nation(models.Model):
    nation_name = models.CharField(
        max_length=255,
        verbose_name='Страны'
    )

    def __str__(self):
        return self.nation_name
    
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Cтраны'