"""Manage views for main app."""

from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        'title': 'Home',
        'welcome': 'Hello World!',
    }
    return render(request, 'main/home.html', context)
