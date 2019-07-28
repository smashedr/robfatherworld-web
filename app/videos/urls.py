from django.urls import path

from videos import views

app_name = 'videos'

urlpatterns = [
    path('tutorials/', views.tutorials_view, name='tutorials'),
    path('speedruns/', views.speedruns_view, name='speedruns'),
    path('livestreams/', views.livestreams_view, name='livestreams'),
]
