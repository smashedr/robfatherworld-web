from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('rfw1/', views.rfw1_view, name='rfw1'),
    path('rfw2/', views.rfw2_view, name='rfw2'),
    path('videos/', views.videos_view, name='videos'),
]
