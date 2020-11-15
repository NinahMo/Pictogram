from django.contrib import admin
from .models import Pics,location,categories

# Register your models here.
admin.site.register(Pics)
admin.site.register(location)
admin.site.register(categories)