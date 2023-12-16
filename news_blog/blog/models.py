from tabnanny import verbose
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Содержание')
    category = models.ForeignKey(category, on_delete=models.)
    image = models.ImageField('Картинка поста', upload_to="post_image/")
    date = models.DateTimeField('Дата создания поста', default=timezone.now())
    slug = models.SlugField('Ссылка', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'