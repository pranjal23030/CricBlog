from django.shortcuts import render,redirect,get_object_or_404
from ..models import Blogs
from django.contrib.auth.decorators import login_required


def home(request):
    blogs = Blogs.objects.all()
    return render(request,'main/home.html',{
        'blogs' : blogs
    })

def single_blog(request, blog_id):
    blog = get_object_or_404(Blogs,pk=blog_id);
    return render(request,"main/single_blog.html", {
        "blog" : blog
    })

@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    
    if blog.author != request.user:
        return redirect("home")

    if request.method == "POST":
        blog.title = request.POST.get("title")
        blog.subtitle = request.POST.get("subtitle")
        blog.description = request.POST.get("description")
        
        if request.FILES.get("image"):
            blog.image = request.FILES.get("image")

        blog.save()
        return redirect("blog_detail", blog_id=blog.id)
    
    return render(request, "main/edit_blog.html", {
        "blog": blog # Giving blog data to edit_blog.html
    })


@login_required
def create_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        subtitle =  request.POST.get("subtitle")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        blog = Blogs(title=title,subtitle=subtitle,description=description,image=image,author=request.user)
        blog.save()
        return redirect("home")
  
    return render(request,"main/create_blog.html")


@login_required
def delete_blog(request,blog_id):
    blog = get_object_or_404(Blogs,pk=blog_id)
    if blog.author == request.user:
        blog.delete()
        return redirect("home")
    else:
        return redirect('blog_detail',blog_id=blog.id)

