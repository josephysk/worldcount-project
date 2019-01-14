

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('eggs/', views.eggs),
    path('dogs/', views.dogs),
    path('count/', views.count, name='count'),
    path('aboutus/', views.aboutus, name='aboutus'),
]
