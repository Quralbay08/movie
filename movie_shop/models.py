from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    category_name = models.CharField(
        max_length=250,
        verbose_name='category_name:'
    )
    category_slug = models.SlugField(
        max_length=250,
        verbose_name='slug:'
    )
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categorys'
    
    def __str__(self):
        return self.category_name

class Janr(models.Model):
    janr_name = models.CharField(
        max_length=250,
        verbose_name='janr_name:'
    )
    janr_slug = models.SlugField(
        max_length=250,
        verbose_name='slug:'
    )
    
    class Meta:
        verbose_name='Janr'
        verbose_name_plural='Janrlar'
    
    def __str__(self):
        return self.janr_name



class Movies(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=250,verbose_name='titile:')
    published_date = models.DateField(verbose_name='date:')
    janr = models.ForeignKey(Janr,on_delete=models.CASCADE)
    description = models.TextField(max_length=250,verbose_name='description:')
    actors = models.TextField(verbose_name='actors:')
    country = models.CharField(max_length=250,verbose_name='country:')
    image = models.ImageField(verbose_name='image:',upload_to='media/posters')
    
    movie=models.FileField(verbose_name='movie_name:',upload_to='media/movies')
    
    class Meta:
        verbose_name='Movie'
        verbose_name_plural='Movies'
    
    def __str__(self):
        return self.title
    
    

class Comments(models.Model):
    text = models.TextField(verbose_name='text:'),
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movies,on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True,verbose_name='comments_date:')
    
    class Meta:
        verbose_name='Comment'
        verbose_name_plural='Comments'
    
    def __str__(self):
        return self.title


