from django.shortcuts import render
from blogs.models import Blog, Category
from assingments.models import About

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status='Publish').order_by('-created_at')
    posts = Blog.objects.filter(is_featured=False, status='Publish')

    #fetch about section
    try:
        about = About.objects.latest('created_at')
    except About.DoesNotExist:
        about = None

    context = { 
       'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request, 'home.html', context)