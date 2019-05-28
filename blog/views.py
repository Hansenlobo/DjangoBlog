from django.shortcuts import render, get_object_or_404
from .models import Blog, Category
from django.db.models import Count, Q

# Create your views here.


def get_category_count():
    queryset=Blog.objects.values('categories__title').annotate(Count('categories'))
    return queryset

def search(request):
    category_count = get_category_count()
    queryset = Blog.objects.all()
    query = request.GET.get('q')
    if query:
        blogs = queryset.filter(Q(title__icontains=query) | Q(overview__icontains=query)).distinct()
    context = {
        'blogs':blogs,
        'query':query,
        'category_count':category_count,
    }
    return render(request, 'search_results.html', context)


def allblogs(request):
    category_count = get_category_count()
    blogs = Blog.objects
    context={
    'category_count':category_count,
    'blogs':blogs
    }
    return render(request, "allblogs.html", context)

def detail(request, post):
    detailblog = get_object_or_404(Blog, slug=post)
    context={
    'detailblog':detailblog,
    }
    return render(request, 'detail.html', context)
