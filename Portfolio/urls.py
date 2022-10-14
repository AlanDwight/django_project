from django.urls import path
from . import views

app_name = 'Portfolio'
urlpatterns = [
    path('', views.portfolio, name='portfolio-home'),
    
]



# <app>/<model>_<viewtype>.html
