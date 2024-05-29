from unittest import TestCase

from dealer_purchase.forms import DealerCreationForm, DealerLicenseUpdateForm


class FormTest(TestCase):
    def test_dealer_creation_with_additional_data_is_valid(self) -> None:
        form_data = {
            "username": "test_user",
            "password1": "12345678910Qaz",
            "password2": "12345678910Qaz",
            "first_name": "Test",
            "last_name": "User",
            "license_number": "ABC12345"
        }
        form = DealerCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_driver_license_update_form_is_valid(self) -> None:
        form_data = {
            "license_number": "ABC11111"
        }

        form = DealerLicenseUpdateForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
