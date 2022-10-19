from django.urls import path
from . import views

app_name = 'Portfolio'
urlpatterns = [
    path('', views.portfolio, name='portfolio-home'),
    path('success/', views.contactView, name='contact-f'),

]


# <app>/<model>_<viewtype>.html
