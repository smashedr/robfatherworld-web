import logging
from django.conf import settings
from django.shortcuts import render
from videos.models import Videos
from videos.twitch import filter_streams

logger = logging.getLogger('app')


def tutorials_view(request):
    #  View: /videos/tutorials/
    videos = Videos.objects.filter(category='tutorials').order_by('-created_at')
    return render(request, 'videos/tutorials.html', {'videos': videos})


def speedruns_view(request):
    #  View: /videos/speedruns/
    videos = Videos.objects.filter(category='speedruns').order_by('-created_at')
    return render(request, 'videos/speedruns.html', {'videos': videos})


def livestreams_view(request):
    #  View: /videos/livestreams/
    streams = filter_streams(settings.TWITCH_CLIENT_ID, search_terms='robfather world')
    return render(request, 'videos/livestreams.html', {'streams': streams})
