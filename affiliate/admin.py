from django.contrib import admin
from . models import Song


# Register your models here.
from .models import Product #Relative import because admin.py and models.py are in the same directory

admin.site.register(Product)
admin.site.register(Song)
