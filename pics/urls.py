from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^images/(\d+)', views.show, name = 'show'),
    url(r'^pictogram/', views.pictogram, name = 'pictogram'),
    url(r'^show/', views.show, name='show'), 
    url(r'^search/', views.search_results, name='search_results')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)