from django.shortcuts import render

# Create your views here.

def index(response):
    """Returns the homepage for pizzeria."""
    return render(response, 'pizzas/index.html')