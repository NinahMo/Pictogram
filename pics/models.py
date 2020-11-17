from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary

# Create your models here.
class Pics(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(max_length=400, null=True, blank=True)
    location = models.ForeignKey('location',on_delete=models.CASCADE)
    categories =models.ForeignKey('categories',on_delete=models.CASCADE, blank=True)
    images = CloudinaryField(default = 'default.jpg')

    def __str__(self):
        return self.name
    
    def save_image(self):
        self.save()

    def update_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class location(models.Model):
    location = models.TextField(max_length=200)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def update_location(self):
        self.update()
    
    def delete_location(self):
        self.delete()

class categories(models.Model):
    categories = models.TextField(max_length=200)

    def __str__(self):
        return self.categories

    def save_categories(self):
        self.save()

    def update_categories(self):
        self.update()

    def delete_categories(self):
        self.delete()

