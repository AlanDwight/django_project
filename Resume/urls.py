from django.urls import path
from . import views 

app_name = 'Resume'
urlpatterns = [
    path('', views.resume_page, name='resume_page'),
]
