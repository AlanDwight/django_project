from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

app_name = 'Blog'
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # page for all posts # home page 
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),   # integer primary key 'int:pk'
                                                # My pk is a string so using a slug converter here intead of int
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),  # page for specific user's posts
]



# <app>/<model>_<viewtype>.html