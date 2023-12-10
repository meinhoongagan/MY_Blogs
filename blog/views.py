from django.shortcuts import render,get_object_or_404
from .models import Post,Category
# Create your views here.
def home(request):
    post=Post.objects.all()[:11]
    category=Category.objects.all()
    data={
        "post":post,
        "category": category,
    }
    return render(request,"index.html",data)
def post(request):
    post=Post.objects.all()
    data={
        "post":post,
        
    }
    return render(request,"post.html",data)
def post_details(request, title):
    post = get_object_or_404(Post, title=title)
    data = {
        "post": post,
    }
    return render(request, "post_details.html", data)
def category_view(request):
    category=Category.objects.all()
    data = {
        "category": category,
    }
    return render(request, "catagory.html", data)