"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from Users import views as user_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('contact/', include('Contact.urls')),
    path('resume/', include('Resume.urls')),
    path('register/', user_view.register, name='register'),
    path('profile/', user_view.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),    #class base view
    path('logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),  #class base view
    path('', include('Blog.urls')),
    path('admin/', admin.site.urls),
] 

if settings.DEBUG:                              #adding this on urlpattern only if we are in debug mode
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


