from django.urls import path
from . import views

urlpatterns = [
    path('', views.listen_view, name="listen"),
    path('audio', views.listen_audio_view, name="listen-audio"),
]
