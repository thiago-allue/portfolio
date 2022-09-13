from django.shortcuts import render
from .models import Article

# Create your views here.

def Index(request):from django.shortcuts import render
from .models import Article

# Create your views here.

def Index(request):
    articles = Article.objects.all()

    return render(request, 'index.html', {'articles':articles})
