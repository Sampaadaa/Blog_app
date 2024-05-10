from django.shortcuts import render
from .models import Post
from django.views.generic import ListView ,DetailView
from django.core.paginator import Paginator



class HomeListView(ListView): 
    model = Post
    template_name = "index.html"
    context_object_name = "posts"  


class AboutListView(ListView): 
    model = Post
    template_name = "aboutme.html"
    context_object_name = "posts" 


class BlogListView(ListView):
 model = Post
 paginate_by=4
 template_name ="blog.html"  

 def get_queryset(self):
        return Post.objects.order_by('-is_featured', '-created_at')

 
class BlogDetailView(DetailView): 
 model = Post
 template_name = "blog_detail.html"    



