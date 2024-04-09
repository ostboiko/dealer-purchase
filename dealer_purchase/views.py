from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from dealer_purchase.forms import ManufacturerSearchForm, ModelCarSearchForm, ModelCarForm, DealerSearchForm, \
    DealerCreationForm, DealerLicenseUpdateForm
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


class ManufacturerListView(LoginRequiredMixin, generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturer_list"
    template_name = "dealer_purchase/manufacturer_list.html"
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
        form = ManufacturerSearchForm(self, request.GET)
        if form.is_valid():
            name_query = form.cleaned_data.get("name")
            if name_query:
                queryset = queryset.filter(name_icontains=name_query)
            return queryset


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("taxi:manufacturer-list")


class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("taxi:manufacturer-list")


class CarListView(LoginRequiredMixin, generic.ListView):
    model = ModelCar
    paginate_by = 5
    queryset = ModelCar.objects.select_related("manufacturer")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        model = self.request.GET.get("model", "")
        context["search_form"] = ModelCarSearchForm(
            initial={"model": model}
        )
        return context

    def get_queryset(self):
        queryset = ModelCar.objects.select_related("manufacturer")
        form = ModelCarSearchForm(self.request.GET)
        if form.is_valid():
            model_query = form.cleaned_data.get("model")
            if model_query:
                queryset = queryset.filter(model__icontains=model_query)
        return queryset


class ModelCarDetailView(LoginRequiredMixin, generic.DetailView):
    model = ModelCar


class ModelCarCreateView(LoginRequiredMixin, generic.CreateView):
    model = ModelCar
    form_class = ModelCarForm
    success_url = reverse_lazy("dealer_purchase:car-list")


class ModelCarUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = ModelCar
    form_class = ModelCarForm
    success_url = reverse_lazy("dealer_purchase:car-list")


class ModelCarDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = ModelCar
    success_url = reverse_lazy("dealer_purchase:car-list")


class DealerListView(LoginRequiredMixin, generic.ListView):
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


class DriverDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dealer
    queryset = Dealer.objects.all().prefetch_related("cars__manufacturer")


class DriverCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dealer
    form_class = DealerCreationForm


class DealerLicenseUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dealer
    form_class = DealerLicenseUpdateForm
    success_url = reverse_lazy("dealer_purchase:driver-list")


class DriverDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dealer
    success_url = reverse_lazy("")


@login_required
def toggle_assign_to_car(request, pk):
    driver = Dealer.objects.get(id=request.user.id)
    if (
        ModelCar.objects.get(id=pk) in driver.cars.all()
    ):  # probably could check if car exists
        driver.cars.remove(pk)
    else:
        driver.cars.add(pk)
    return HttpResponseRedirect(reverse_lazy("dealer_purchase:car-detail", args=[pk]))
