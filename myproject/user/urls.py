from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('services/',views.services),
    path('video/',views.videogallery),
    path('viewsnews/',views.newsd),
    path('viewmore/',views.viewmore),
    path('Attacks/',views.Attacks),
    path('Devices/',views.Devices),
    path('Country/',views.Country),
    path('IT News/',views.IT_News),
]
