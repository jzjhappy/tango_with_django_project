from django.db import models
import hashlib


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    hashedname = models.CharField(max_length=64, unique=True)

    def save(self, *args, **kwargs):
        self.hashedname = hashlib.sha256((self.name).encode('utf-8')).hexdigest()
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    contactphone = models.CharField(max_length=15)
    
    def __str__(self):
        return self.title