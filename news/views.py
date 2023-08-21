from django.views.generic import ListView,DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = 'name'
    template_name = 'post.html'
    context_object_name = 'post'
    
class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    
