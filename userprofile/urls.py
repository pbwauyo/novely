from . import views
from django.urls import path

urlpatterns = [
    path('', views.user_profile, name='profile'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('subscriptions/hours/100', views.subscription_100, name='subscription-100'),
    path('subscriptions/hours/200', views.subscription_200, name='subscription-200'),
    path('subscriptions/hours/100/done/', views.subscription_100_done, name='subscription-100-done'),
    path('subscriptions/hours/200/done/', views.subscription_200_done, name='subscription-200-done'),
]
