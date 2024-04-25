from django.urls import path

from .views import (
    index,
    toggle_assign_to_car,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    DealerListView,
    DealerDetailView,
    DealerCreateView,
    DealerLicenseUpdateView,
    DealerDeleteView, CityListView, CityCreateView, CityUpdateView, CityDeleteView, CarListView, CarDetailView,
    CarCreateView, CarUpdateView, CarDeleteView, CityDetailView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "manufacturers/",
        ManufacturerListView.as_view(),
        name="manufacturer-list",
    ),
    path(
        "manufacturers/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturers/<int:pk>/update/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path(
        "manufacturers/<int:pk>/delete/",
        ManufacturerDeleteView.as_view(),
        name="manufacturer-delete",
    ),
    path("cars/", CarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", CarDetailView.as_view(), name="car-detail"),
    path("cars/create/", CarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/update/", CarUpdateView.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/", CarDeleteView.as_view(), name="car-delete"),
    path(
        "cars/<int:pk>/toggle-assign/",
        toggle_assign_to_car,
        name="toggle-car-assign",
    ),
    path("dealers/", DealerListView.as_view(), name="dealer-list"),
    path(
        "dealers/<int:pk>/", DealerDetailView.as_view(), name="dealer-detail"
    ),
    path("dealers/", DealerListView.as_view(), name="dealer-list"),
    path(
        "dealers/<int:pk>/", DealerDetailView.as_view(), name="dealer-detail"
    ),
    path("dealers/create/", DealerCreateView.as_view(), name="dealer-create"),
    path(
        "dealers/<int:pk>/update/",
        DealerLicenseUpdateView.as_view(),
        name="dealer-update",
    ),
    path(
        "dealer/<int:pk>/delete/",
        DealerDeleteView.as_view(),
        name="dealer-delete",
    ),

    path("cities/", CityListView.as_view(), name="city-list"),
    path('cities/<int:pk>/',CityDetailView.as_view(), name='city-detail'),
    path("cities/create/", CityCreateView.as_view(), name="city-create"),
    path("cities/<int:pk>/update/", CityUpdateView.as_view(), name="city-update"),
    path("cities/<int:pk>/delete/", CityDeleteView.as_view(), name="city-delete"),
    path(
        "cities/<int:pk>/toggle-assign/",
        toggle_assign_to_car,
        name="toggle-car-assign",
    ),
]

app_name = "dealer"
