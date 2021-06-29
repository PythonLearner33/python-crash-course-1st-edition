from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for meal_planning."""
    return render(request, 'meal_planning/index.html')