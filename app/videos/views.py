import logging
from django.shortcuts import render
from videos.models import Videos

logger = logging.getLogger('app')


def index_view(request):
    #  View: /videos/
    return render(request, 'videos/videos.html')


def tutorials_view(request):
    #  View: /videos/tutorials/
    videos = Videos.objects.all().order_by('-created_at')
    return render(request, 'videos/tutorials.html', {'videos': videos})
