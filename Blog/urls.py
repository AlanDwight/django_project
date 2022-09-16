from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

app_name = 'Blog'
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),   # integer primary key 'int:pk'
                                                # My pk is a string so using a slug converter here intead of int
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
]



# <app>/<model>_<viewtype>.html