from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/media', blank=True)
    date = models.DateTimeField()
    locate = models.CharField(max_length=30)
    descriptions = models.TextField(max_length=150)
    full_descriptions = models.TextField(max_length=500)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-date']