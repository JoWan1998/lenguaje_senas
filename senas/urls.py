from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video', views.video, name='video'),
    path('stream', views.stream, name='stream'),
    path('stream_solution', views.stream_hand, name='stream_solution')
    
]