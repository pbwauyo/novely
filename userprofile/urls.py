from . import views
from django.urls import path

urlpatterns = [
    path('', views.user_profile, name='profile')  ,
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('subscriptions/hours/', views.subscription_hours, name='subscription-hours'),
    path('subscriptions/days/', views.subscription_days, name='subscription-days'),
    path('subscriptions/hours/done/', views.subscription_hours_done, name='subscription-hours-done'),
    path('subscriptions/days/done/', views.subscription_days_done, name='subscription-days-done'),
]
