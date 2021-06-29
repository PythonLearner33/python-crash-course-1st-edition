from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # Gets current date and time and sets it permanently.

    def __str__(self):
        return self.title # Necessary for when viewing in admin site; otherwise returns 'BlogPost object'.