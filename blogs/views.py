from django.shortcuts import get_object_or_404, render
from .models import Blog, Category
from django.db.models import Q

# Create your views here.




def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status='Published', category=category_id)
    # Use try/except when we want to do some custom action if the category does not exists
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect the user to homepage
    #     return redirect('home')
    
    # Use get_object_or_404 when you want to show 404 error page if the category does not exist
    category = get_object_or_404(Category, pk=category_id)
    
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    # Fetch the blog post with the given slug
    single_blog = get_object_or_404(Blog, slug=slug, status='Publish')
    
    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html', context)


def search(request):
    query = request.GET.get('keyword', 'q')  # Get the search query from the request parameters
    if query:
       ## Search for blog posts that contain the query in their title or content
       results = Blog.objects.filter(status='Published').filter(
            Q(title__icontains=query) | Q(short_description__icontains=query)| Q(blog_body__icontains=query), status='Publish')
    else:
        results = Blog.objects.none()  # Return an empty queryset if no query is provided

    context = {
        'results': results,
        'query': query,
    } 
    return render(request, 'search.html', context)
