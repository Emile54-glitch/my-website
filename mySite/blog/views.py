from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'object_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'