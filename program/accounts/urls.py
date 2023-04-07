from django.contrib import admin
from django.urls import path, include
from .views import home, about

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]

