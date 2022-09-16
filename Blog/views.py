from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # if you tried to make new post without login you will be redirected to login page 
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView

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

    # function view (not class view)(not list view)
]
def home(request):    # we don't use the home function call anymore, we now using the class view
    context = { 
        'posts' : Post.objects.all(),     #getting data from 'Post' model database
        'title' : 'Posts'
    }
    return render(request, 'Blog/home.html', context)


class PostListView(ListView):   # making listview
    model = Post
    template_name = 'Blog/home.html'   # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'  # changing the attribute that class is searching for to 'posts', without that, class will search 'default' list object
    ordering = ['-date_posted']  #  latest to oldest ordering 

class PostCreateView(LoginRequiredMixin, CreateView):   # 'LoginRequiredMixin' if you tried to make new post without login you will be redirected to login page
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): 
        form.instance.author = self.request.user   # set instance to current log in user
        return super().form_valid(form)  # overwriting the parent method

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):   # 'LoginRequiredMixin' if you tried to make new post without login you will be redirected to login page
    model = Post
    fields = ['title', 'content']      # updating the information of existing post

    def form_valid(self, form): 
        form.instance.author = self.request.user   # set instance to current log in user
        return super().form_valid(form)  # overwriting the parent method

    def test_func(self):            # checking if the user is the valid for editing the post else deny from updating
        post = self.get_object()    # getting current post's user instance object
        if self.request.user == post.author: # comparing request user instance and post user instance if true allow update else deny
            return True 
        return False 

    
class PostDetailView(DetailView):   # making listview
    model = Post  # Blog/post_detail.html

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):   # making listview
    model = Post  # Blog/post_detail.html
    success_url = '/'
    def test_func(self):            # checking if the user is the valid for editing the post else deny from updating
        post = self.get_object()    # getting current post's user instance object
        if self.request.user == post.author: # comparing request user instance and post user instance if true allow update else deny
            return True 
        return False

def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})
