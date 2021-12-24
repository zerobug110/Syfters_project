from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(default= datetime.now, blank=True)
    thumbnail_1 = models.ImageField(upload_to='media')
    thumbnail_2 = models.ImageField(upload_to='media')
    thumbnail_3 = models.ImageField(upload_to='media')
    thumbnail_4 = models.ImageField(upload_to='media')  

    def __str__(self):
        return self.name



class About(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

class New(models.Model):
    title = models.CharField(max_length=255)
    time = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title



class LatestNew(models.Model):
    title = models.CharField(max_length=255)
    time = models.DateField()
    content = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title
    def save(self, *args,**kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)
        