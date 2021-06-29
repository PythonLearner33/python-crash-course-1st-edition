from django.contrib import admin

from .models import BlogPost

# Register your models here.

admin.site.register(BlogPost) # I forgot to register my model; don't forget this.