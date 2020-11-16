from django.shortcuts import render, redirect
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

def search_results(request):

    if 'categories' in request.GET and request.GET["categories"]:
        search_term = request.GET.get("categories")
        searched_categories = categories.search_by_categories(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})