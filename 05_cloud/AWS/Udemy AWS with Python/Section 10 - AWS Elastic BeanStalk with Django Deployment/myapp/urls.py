from django.test import TestCase

# Create your tests here.

from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index, name='index'),
]
