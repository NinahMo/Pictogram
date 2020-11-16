from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Pics

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def pictogram(request):
    images = Pics.objects.all()
    return render(request, 'pictogram.html', {'images':images})

def show(request, image_id):
    image = Pics.objects.get(id=image_id)
    return render(request, 'show.html', {'image':image})
