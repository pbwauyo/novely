from . import views
from django.urls import path

urlpatterns = [
     path('', views.login_initial, name='login-initial'),
     path('login/',views.login_view ,name='login'),
     path('signup/', views.signup_view, name='signup'),
     path('logout/',views.logout_view ,name='logout'),
     path('logout-user/', views.logout_user, name='logout-user'),   
]
