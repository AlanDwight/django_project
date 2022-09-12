from django.urls import path
from . import views 

app_name = 'Contact'
urlpatterns = [
    path('address/', views.index, name='index'),
]