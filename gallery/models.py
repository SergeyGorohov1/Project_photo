from django.db import models
from filer.fields.image import FilerImageField


class Photo(models.Model):
    filename = models.CharField(max_length=255, verbose_name="Название файла", null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name="Название изображения")

    image = FilerImageField(on_delete=models.SET_NULL, related_name='image', null=True, blank=True,
                            verbose_name="Изображение")

    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата и время изменения")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
