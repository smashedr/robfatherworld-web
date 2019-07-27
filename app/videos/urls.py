from django.urls import path

from videos import views

app_name = 'videos'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('tutorials/', views.tutorials_view, name='tutorials'),
]
