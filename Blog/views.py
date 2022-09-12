from django.shortcuts import render
from django.http import HttpResponse
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
def home(request):
    context = { 
        'posts' : Post.objects.all(),     #getting data from 'Post' model database
        'title' : 'Posts'
    }
    return render(request, 'Blog/home.html', context)


def about(request):
    return render(request, 'Blog/about.html', {'title': 'About'})
