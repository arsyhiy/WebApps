from django.db import models

# Create your models here.

class Post(models.Model):
    """данные о посте"""
    title = models.CharField('загаловок записи', max_length=50)
    description = models.TextField('текст записи', max_length=500)
    author = models.CharField('имя автора', max_length=50)
    date = models.DateField('дата публикации')
    img = models.ImageField('изображения', upload_to='image/%Y')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return f'{self.title}, {self.author}'
    
    

class Comments(models.Model):
    """коментарии"""
    email = models.EmailField()
    name = models.CharField('имя', max_length=50)
    text_comments = models.TextField('текст коментария', max_length=1000)
    post = models.ForeignKey(Post, verbose_name='публикация', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return f'{self.name}, {self.post}'
    

class Likes(models.Model):
    """likes"""
    ip = models.CharField('IP-adres', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='publication', on_delete=models.CASCADE)
    