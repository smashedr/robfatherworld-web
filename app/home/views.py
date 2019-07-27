import logging
from django.shortcuts import render

logger = logging.getLogger('app')


def home_view(request):
    #  View: /
    return render(request, 'home.html')


def about_view(request):
    #  View: /videos/
    return render(request, 'about.html')


def rfw1_view(request):
    #  View: /videos/
    return render(request, 'rfw1.html')


def rfw2_view(request):
    #  View: /videos/
    return render(request, 'rfw2.html')
