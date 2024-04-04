from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from dealer_purchase.models import Dealer, ModelCar, Manufacturer, City


@login_required
def index(request):
    """View function for the home page of the site."""

    num_dealers = Dealer.objects.count()
    num_cars = ModelCar.objects.count()
    num_manufacturers = Manufacturer.objects.count()
    num_cities = City.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_dealers": num_dealers,
        "num_cars": num_cars,
        "num_manufacturers": num_manufacturers,
        "num_cities": num_cities,
        "num_visits": num_visits + 1,
    }

    return render(request, "dealer_purchase/index.html", context=context)
