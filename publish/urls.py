from . import views
from django.urls import path

urlpatterns = [
    path('', views.publish, name='publish'),
    path('publish-new/<int:pk>/', views.publish_new, name='publish-new'),
    path('accept-license/<int:pk>/', views.accept_license, name='accept-license'),
    path('publish-done/<int:pk>/', views.publish_done, name='publish-done'),
    path('new-audio/', views.new_audio, name='new-audio'),
]
