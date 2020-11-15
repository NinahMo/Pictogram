from django.db import models

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(max_lemgth=400, null=True, blank=True)
    location = models.ForeignKey('location',on_delete=models.CASCADE)
    categories = models.ForeignKey('categories',on_delete=models.CASCADE)
    