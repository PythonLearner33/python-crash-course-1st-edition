from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views # From the same folder, import views.py

app_name = 'blogs' # We define this variable to connect with Django.

urlpatterns = [
    path('', views.index, name='index'), # Homepage
    path('create_post', views.create_post, name='create_post'), # Create Blog Post
    path('edit_post/<int:blog_id>', views.edit_post, name='edit_post'), # Edit Blog Post
]

urlpatterns += staticfiles_urlpatterns() # Include static file URL patterns.