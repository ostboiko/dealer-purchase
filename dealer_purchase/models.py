from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.urls import reverse


class Dealer(AbstractUser):
    name = models.CharField(unique=True, max_length=255)
    license_number = models.CharField(max_length=255, unique=True)
    user_permissions = models.ManyToManyField(Permission, related_name='dealer_user_permissions')
    groups = models.ManyToManyField(Group, related_name='dealer_groups')

    class Meta:
        app_label = 'dealer_purchase'
        verbose_name = "dealer"
        verbose_name_plural = "dealers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("dealer_purchase:dealer-detail", kwargs={"pk": self.pk})


class Manufacturer(models.Model):
    name = models.CharField(unique=True, max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.country}"


class Car(models.Model):
    car = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.car


class City(models.Model):
    city = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.city
