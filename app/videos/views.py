import logging
from django.shortcuts import render
from videos.models import Videos

logger = logging.getLogger('app')


def tutorials_view(request):
    #  View: /videos/tutorials/
    videos = Videos.objects.filter(category='tutorials').order_by('-created_at')
    return render(request, 'videos/tutorials.html', {'videos': videos})


def speedruns_view(request):
    #  View: /videos/speedruns/
    videos = Videos.objects.filter(category='speedruns').order_by('-created_at')
    return render(request, 'videos/speedruns.html', {'videos': videos})
