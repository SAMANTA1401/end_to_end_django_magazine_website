from django.db import models


# Create your models here.

class Magazine(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    authname = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    img = models.ImageField( blank=True,null=True)
    pdffile = models.FileField(  blank=True, null=True)
    read = models.IntegerField(default=0)
    download = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=255)
    authname = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    img = models.ImageField(blank=True, null=True)
    pdf = models.FileField(blank=True, null=True)
    download = models.IntegerField(default=0)
    actual_price = models.FloatField(default=0)
    on_price = models.FloatField(default=0)

    def __str__(self):
        return self.title

class Podcast(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2000)
    authname = models.CharField(max_length=255)
    voice = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    img = models.ImageField( blank=True, null=True)
    spotify_link = models.CharField(max_length=300, null=True)
    youtube_link = models.CharField(max_length=300, null=True)
    listener = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class WebCount(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.count)
