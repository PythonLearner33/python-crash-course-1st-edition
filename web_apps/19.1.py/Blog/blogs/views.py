from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def index(request):
    """Returns the blog homepage when requested by browser."""
    blogs = BlogPost.objects.order_by('-date') # Gather all BlogPost objects by date.

    context = {'blogs':blogs} # Declare context variable so Django can use it.
    return render(request, 'blogs/index.html', context) # Render and return index.html with context variable loaded in.

def blog_post(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, 'blogs/blog_post.html', context)

def create_post(request):
    if request.method != "POST":
        form = BlogPostForm()
        context = {'form': form}
        return render(request, 'blogs/create_post.html', context) # i switched the syntax. it works.
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))

def edit_post(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    if request.method != "POST":
        form = BlogPostForm(instance=blog)
    else:
        form = BlogPostForm(instance=blog, data=request.POST) # Prefill a new form with an instance of 
                                                              # blog. Update changes with new data from POST.
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:blog_post', args=[blog.id]))
    context = {'blog':blog,'form':form} # blog is used for the form.
    return render(request, 'blogs/edit_post.html', context)