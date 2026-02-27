from django.db import models
from filer.fields.image import FilerImageField


class Photo(models.Model):
    image = FilerImageField(on_delete=models.CASCADE, related_name='image', verbose_name="Изображение")

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
