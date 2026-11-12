from django.shortcuts import render
from .models import Post
from django.db.models import Q

# Create your views here.
def post_list(request):
    query = request.GET.get('q') # search keywords
    catagory = request.GET.get('catagory') # catagory filter

    posts = Post.objects.all()

    #search using q object 
    if query:
        posts = posts.filter(
            Q(title__icontains = query) |
            Q(content__icontains = query)
        )

    #filter by catagoty
    if catagory:
        posts = posts.filter(catagory__iexact=catagory)

    return render(request, 'blog/post_list.html',{
        'posts':posts,
        'query':query,
        'catagory':catagory,
        })