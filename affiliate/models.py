from django.db import models

# Create your models here.
class Product(models.Model):# you can change Products to the name of the things you are selling
    title       = models.CharField(max_length = 120)
    description = models.TextField(default = 'Starndard Class of Minimalist')
    price       = models.DecimalField(decimal_places=2,max_digits=1000)
    summary     = models.TextField(default = 'Awesome products')
    feauture    = models.BooleanField(default = True)

class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    audio_link = models.CharField(max_length=200,blank=True,null=True)
    duration=models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.title
