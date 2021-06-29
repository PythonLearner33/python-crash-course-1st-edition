from django.urls import path

from . import views # From the same folder, import views.py

app_name = 'blogs' # We define this variable to connect with Django.

urlpatterns = [
    path('', views.index, name='index'), # Homepage
    path('blog_post/<int:blog_id>', views.blog_post, name='blog_post'), # Specific Blog Post
    path('create_post', views.create_post, name='create_post'), # Create Blog Post
    path('edit_post/<int:blog_id>', views.edit_post, name='edit_post'), # Edit Blog Post
]