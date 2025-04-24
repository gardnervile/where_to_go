from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название места'
    )
    short_description = models.TextField(
        blank=True,
        verbose_name='Краткое описание'
    )
    long_description = HTMLField(
        blank=True,
        verbose_name='Полное описание (HTML)'
    )
    latitude = models.FloatField(
        verbose_name='Широта'
    )
    longitude = models.FloatField(
        verbose_name='Долгота'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name='Место'
    )
    image = models.ImageField(
        upload_to='place_images/',
        verbose_name='Изображение'
    )
    position = models.PositiveIntegerField(
        default=0,
        verbose_name='Позиция',
        db_index=True
    )

    class Meta:
        ordering = ['position']
        verbose_name = 'Фотография места'
        verbose_name_plural = 'Фотографии места'

    def __str__(self):
        return f'{self.place.title} — Фото {self.position}'
