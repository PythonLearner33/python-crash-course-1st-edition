from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def index(request):
    """Returns the blog homepage when requested by browser."""
    blogs = BlogPost.objects.order_by('-date') # Gather all BlogPost objects by date.
    current_user = request.user
    context = {'blogs':blogs, 'current_user':current_user} # Declare context variable so Django can use it.
    return render(request, 'blogs/index.html', context) # Render and return index.html with context variable loaded in.

def blog_post(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    context = {'blog': blog}
    return render(request, 'blogs/blog_post.html', context)

@login_required
def create_post(request):
    if request.method != "POST":
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:index'))
    context = {'form': form}
    return render(request, 'blogs/create_post.html', context)

@login_required
def edit_post(request, blog_id):
    blog = BlogPost.objects.get(id=blog_id)
    if request.user != blog.owner:
        raise Http404
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