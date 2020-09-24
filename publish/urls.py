from . import views
from django.urls import path

urlpatterns = [
    path('', views.publish, name='publish'),
    path('publish-new', views.publish_new, name='publish-new'),
]
