from django.urls import path

from .views import (
    index,
    toggle_assign_to_car,
    ManufacturerListView,
    ManufacturerCreateView,
    ManufacturerUpdateView,
    ManufacturerDeleteView,
    ModelCarListView,
    ModelCarDetailView,
    ModelCarCreateView,
    ModelCarUpdateView,
    ModelCarDeleteView,
    DealerListView,
    DealerDetailView,
    DealerCreateView,
    DealerLicenseUpdateView,
    DealerDeleteView,
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
    path("cars/", ModelCarListView.as_view(), name="car-list"),
    path("cars/<int:pk>/", ModelCarDetailView.as_view(), name="car-detail"),
    path("cars/create/", ModelCarCreateView.as_view(), name="car-create"),
    path("cars/<int:pk>/update/", ModelCarUpdateView.as_view(), name="car-update"),
    path("cars/<int:pk>/delete/", ModelCarDeleteView.as_view(), name="car-delete"),
    path(
        "cars/<int:pk>/toggle-assign/",
        toggle_assign_to_car,
        name="toggle-car-assign",
    ),
    path("dealers/", DealerListView.as_view(), name="driver-list"),
    path(
        "dealers/<int:pk>/", DealerDetailView.as_view(), name="driver-detail"
    ),
    path("dealers/", DealerListView.as_view(), name="driver-list"),
    path(
        "dealers/<int:pk>/", DealerDetailView.as_view(), name="driver-detail"
    ),
    path("dealers/create/", DealerCreateView.as_view(), name="driver-create"),
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
]

app_name = "dealer"
