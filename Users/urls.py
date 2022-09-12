from django.urls import path
from . import views

app_name = 'Users'
urlpatterns = [
    path('', views.home, name='user-home'),
    path('about/', views.about, name='user-about'),
]
