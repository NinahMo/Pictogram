from django.db import models

# Create your models here.
class Pics(models.Model):
    name = models.CharField(max_length=400, null=True, blank=True)
    description = models.TextField(max_length=400, null=True, blank=True)

