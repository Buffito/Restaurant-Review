from django.http import request
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    allRestaurants = Restaurant.objects.all()
    
    context = {
        "restaurants": allRestaurants,
    }

    return render(request, 'main/index.html', context)


#details page
def detail(request, id):
    restaurant = Restaurant.objects.get(id=id)

    context = {
        "restaurant": restaurant
    }

    return render(request, 'main/details.html', context)


#add restaurant
def add_restaurant(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST or None)

        if form.is_valid:
            data = form.save(commit=False)
            data.save
            return redirect("main:home")

    else:
        form = RestaurantForm()
    return render(request, 'main/addrestaurant.html', {"form": form , "controller": "Προσθήκη Εστιατορίου"})


#edit restaurant
def edit_restaurant(request, id):
    restaurant = Restaurant.objects.get(id=id)

    if request.method == "POST":
        form = RestaurantForm(request.POST or None, instance=restaurant)
                
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("main:detail", id)
        
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'main/addrestaurant.html', {"form": form, "controller": "Επεξεργασία Εστιατορίου"})

#delete restaurant
def delete_restaurant(request, id):
    restaurant = Restaurant.objects.get(id=id)

    restaurant.delete()
    return redirect("main:home")