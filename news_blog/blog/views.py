from django.http import HttpResponse
from django.shortcuts import render
from .models imports Post


def index(request):
    posts = Post.objects.order_by('-date')[:5]
    categories = category.objects.all(wd)
    return render(request, 'index.html'), {'posts':}