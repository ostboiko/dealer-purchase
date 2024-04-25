from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DetailView

from dealer_purchase.forms import ManufacturerSearchForm, CarSearchForm, CarForm, DealerSearchForm, \
    DealerCreationForm, DealerLicenseUpdateForm, CitySearchForm, CarForm
from dealer_purchase.models import Dealer, Car, Manufacturer, City, Car


@login_required
def index(request):
    """View function for the home page of the site."""

    num_dealers = Dealer.objects.count()
    num_cars = Car.objects.count()
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

    return render(request, "dealer/index.html", context=context)


class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "dealer/manufacturer_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ManufacturerListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = ManufacturerSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Manufacturer.objects.all()
        form = ManufacturerSearchForm(self.request.GET)
        if form.is_valid():
            name_query = form.cleaned_data.get("name")
            if name_query:
                queryset = queryset.filter(
                    name__icontains=name_query)
        return queryset


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("dealer:manufacturer-list")


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("dealer:manufacturer-list")


class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("dealer:manufacturer-list")


class CarListView(LoginRequiredMixin, generic.ListView):
    template_name = 'dealer/car_list.html'
    model = Car
    paginate_by = 5
    queryset = Car.objects.select_related("manufacturer")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        model = self.request.GET.get("model", "")
        context["search_form"] = CarSearchForm(
            initial={"model": model}
        )
        return context

    def get_queryset(self):
        queryset = Car.objects.select_related("manufacturer")
        form = CarSearchForm(self.request.GET)
        if form.is_valid():
            model_query = form.cleaned_data.get("model")
            if model_query:
                queryset = queryset.filter(model__icontains=model_query)
        return queryset


class CarDetailView(LoginRequiredMixin, generic.DetailView):
    model = Car


class CarCreateView(LoginRequiredMixin, generic.CreateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("dealer:car-list")


class CarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Car
    form_class = CarForm
    success_url = reverse_lazy("dealer:car-list")


class CarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Car
    success_url = reverse_lazy("dealer:car-list")


class DealerListView(LoginRequiredMixin, generic.ListView):
    template_name = 'dealer/dealer_list.html'
    model = Dealer
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = DealerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = DealerSearchForm(self.request.GET)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get("username")
            if username:
                queryset = queryset.filter(username__icontains=username)
        return queryset


class DealerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dealer
    queryset = Dealer.objects.all().prefetch_related("cars__manufacturer")


class DealerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dealer
    form_class = DealerCreationForm


class DealerLicenseUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dealer
    form_class = DealerLicenseUpdateForm
    success_url = reverse_lazy("dealer:driver-list")


class DealerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dealer
    success_url = reverse_lazy("")


class CityListView(LoginRequiredMixin, generic.ListView):
    model = City
    context_object_name = "city_list"
    template_name = "dealer/city_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CityListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = CitySearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = City.objects.all()
        form = CitySearchForm(self.request.GET)
        if form.is_valid():
            name_query = form.cleaned_data["query"]
            if name_query:
                queryset = queryset.filter(city__icontains=name_query)
            return queryset


class CityDetailView(DetailView):
    model = City
    template_name = 'dealer/city_detail.html'
    context_object_name = 'city'


class CityCreateView(LoginRequiredMixin, generic.CreateView):
    model = City
    fields = "__all__"
    success_url = reverse_lazy("dealer_purchase:city-list")


class CityUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = City
    fields = "__all__"
    success_url = reverse_lazy("dealer_purchase:city-list")


class CityDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = City
    success_url = reverse_lazy("dealer_purchase:manufacturer-list")


@login_required
def toggle_assign_to_car(request, pk):
    dealer = Dealer.objects.get(id=request.user.id)
    if (
        Car.objects.get(id=pk) in dealer.cars.all()
    ):
        dealer.cars.remove(pk)
    else:
        dealer.cars.add(pk)
    return HttpResponseRedirect(reverse_lazy("dealer:car-detail", args=[pk]))
