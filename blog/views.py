
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def index(request):
    selected_posts = Post.objects.all().order_by('-date')[:3]
    return  render(request, 'blog/index.html', {
        'posts': selected_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/posts.html', {
        'posts': all_posts
    })

def post_detail(request, slug):
    post_specified = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {
        "post": post_specified
    })
