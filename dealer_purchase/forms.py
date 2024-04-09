from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from dealer_purchase.models import ModelCar, Dealer


class ModelCarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = ModelCar
        fields = "__all__"


class DealerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Dealer
        fields = UserCreationForm.Meta.fields + (
            "license_number",
            "first_name",
            "last_name",
        )

    def clean_license_number(self):  # this logic is optional, but possible
        return validate_license_number(self.cleaned_data["license_number"])


class DealerLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = ["license_number"]

    def clean_license_number(self):
        return validate_license_number(self.cleaned_data["license_number"])


def validate_license_number(
    license_number,
):  # regex validation is also possible here
    if len(license_number) != 8:
        raise ValidationError("License number should consist of 8 characters")
    elif not license_number[:3].isupper() or not license_number[:3].isalpha():
        raise ValidationError("First 3 characters should be uppercase letters")
    elif not license_number[3:].isdigit():
        raise ValidationError("Last 5 characters should be digits")

    return license_number


class SearchForm(forms.Form):
    query = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search"})
    )


class DealerSearchForm(SearchForm):
    pass


class ModelCarSearchForm(SearchForm):
    pass


class ManufacturerSearchForm(SearchForm):
    pass
