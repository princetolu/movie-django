from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100, blank=True)
    description=models.TextField(max_length=1000, blank=True)
    cover=models.ImageField(upload_to='images', default='', blank=True)
    bg_img=models.ImageField(upload_to='images', default='', blank=True)
    video_link=models.CharField(max_length=1000, default= '', blank=True)
    year=models.CharField(max_length=4, default= '', blank=True)
    mins=models.CharField(max_length=3, default= '', blank=True)
    rating=models.CharField(max_length=3, default= '', blank=True)
    genere=models.CharField(max_length=1000, blank=True)
    date=models.DateTimeField()

    def __str__(self):
        return self.title
    