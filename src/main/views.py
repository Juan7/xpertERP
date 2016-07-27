"""Manage views for main app."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

@login_required
def home(request):
    context = {
        'title': 'Home',
        'welcome': 'Hello World!',
    }
    return render(request, 'main/home.html', context)
