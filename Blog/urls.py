from django.urls import path
from . import views

app_name = 'Blog'
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
