# Generated by Django 4.1.1 on 2022-10-02 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0007_alter_booking_options_booking_hotel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Забронированый отель', 'verbose_name_plural': 'Забронированые отели'},
        ),
    ]
