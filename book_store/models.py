from django.db import models

# Create your models here.


class book(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название книги')
    description = models.TextField(blank=True, null=True, verbose_name='Описание книги')
    count_pages = models.IntegerField(null=True, verbose_name='Количество страниц')
    price = models.FloatField(verbose_name='Цена')
    cover_type = models.CharField(max_length=50, null=True, verbose_name='Тип обложки')
    size = models.CharField(max_length=50, null=True, verbose_name='Размер книги')
    publication_date = models.DateField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title', 'publication_date']





