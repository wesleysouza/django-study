from django.urls import path

from .views import index, contact

urlpatterns = [
    path('', index),
    path('contact', contact),
]