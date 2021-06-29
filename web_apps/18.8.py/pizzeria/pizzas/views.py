from django.shortcuts import render

from .models import Pizza
# Create your views here.

def index(response):
    """Returns the homepage for pizzeria."""
    return render(response, 'pizzas/index.html')

def menu(response):
    """Returns the menu for pizzeria."""
    pizzas = Pizza.objects.all()
    context = {'pizzas':pizzas}
    return render(response, 'pizzas/menu.html', context)

def toppings(response, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = {"pizza":pizza, "toppings":toppings}
    return render(response, 'pizzas/toppings.html', context)