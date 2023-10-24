from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # if you tried to make new post without login you will be redirected to login page 
from django.contrib.auth.models import User
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView, 


)   #list view (class base view)

from .models import Post
 
# Create your views here.

posts = [
    {
        'author' : 'someone', 
        'title'  : 'sometitle',
        'content': 'somecontent',
        'date_posted': 'August 27'
    },
    {
        'author' : 'someone1', 
        'title'  : 'sometitle1',
        'content': 'somecontent1',
        'date_posted': 'August 28'
    } 

]

 # function base view (not class view)(not list view)

def home(request):    # we don't use the home function call anymore, we now using the class view
    context = { 
        'posts' : Post.objects.all(),     #getting data from 'Post' model database
        'title' : 'Posts'
    }
    return render(request, 'Blog/home.html', context)

 # making listview   # aka class base view

class PostListView(ListView):
    model = Post
    template_name = 'Blog/home.html'   # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  # changing the attribute that class is searching for to 'posts', without that, class will search 'default' list object
    ordering = ['-date_posted']  #  latest to oldest ordering 
    paginate_by = 4 # two post per page (pagination)

class UserPostListView(ListView):
    model = Post
    template_name = 'Blog/user_posts.html'   # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  # changing the attribute that class is searching for to 'posts', without that, class will search 'default' list object
    #ordering = ['-date_posted']  #  latest to oldest ordering 
    paginate_by = 4 # four posts per page (pagination)

    def get_queryset(self):   # filtering method for the single user's posts   
        user = get_object_or_404(User, username = self.kwargs.get('username')) # kwargs are query parameter from url  # if user in url exist then store in user var and return user data from 'Post' model else then return 404 error
        return Post.objects.filter(author = user).order_by('-date_posted')   # reordering the posts of individual user
 
 # class base view can't be used with decorator

class PostCreateView(LoginRequiredMixin, CreateView):   # 'LoginRequiredMixin' if you tried to make new post without login you will be redirected to login page
    model = Post
    fields = ['title', 'content']
    #success_url = 'Blog/home.html' #landing on the home page instead of detail view of post by get_absolute_url

    def form_valid(self, form): 
        form.instance.author = self.request.user   # set instance to current log in user
        return super().form_valid(form)  # overwriting the parent method

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):   # 'LoginRequiredMixin' if you tried to make new post without login you will be redirected to login page
    model = Post
    fields = ['title', 'content']      # updating the information of existing post

    def form_valid(self, form): 
        form.instance.author = self.request.user   # set instance to current log in user
        return super().form_valid(form)  # overwriting the parent method

    def test_func(self):    #require funtion for UserPassesTestMixin # checking if the user is the valid for editing the post else deny from updating
        post = self.get_object()    # getting current post's user instance object
        if self.request.user == post.author: # comparing request user instance and post user instance if true allow update else deny
            return True 
        return False 

    
class PostDetailView(DetailView):   # making listview   # the individual view for each post 
    model = Post  # Blog/post_detail.html    # <app>/<model>_<viewtype>.html

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):   # making listview  # func for post deletion and warning 
    model = Post  # Blog/post_detail.html
    success_url = '/blog/'
    def test_func(self):            # checking if the user is the valid for editing the post else deny from updating
        post = self.get_object()    # getting current post's user instance object
        if self.request.user == post.author: # comparing request user instance and post user instance if true allow update else deny
            return True 
        return False

# funtion base view 

def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})
