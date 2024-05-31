from django.test import TestCase

import dealer_purchase
from dealer_purchase.models import Manufacturer, Dealer, Car


class ModelTests(TestCase):
    def test_manufacturer_str(self) -> None:
        manufacturer = Manufacturer.objects.create(
            name="BMW",
            country="Germany"
        )

        self.assertEqual(
            str(manufacturer),
            f"{manufacturer.name} {manufacturer.country}"
        )

    def test_driver_str(self) -> None:
        dealer = Dealer.objects.create(
            username="test_user",
            password="12345678910Qaz",
            first_name="Test",
            last_name="User"
        )

        self.assertEqual(
            str(dealer_purchase),
            f"{dealer.name} ({dealer.first_name} {dealer.last_name})"
        )

    def test_driver_with_license_number(self) -> None:
        license_number = "ABC12345"

        dealer = Dealer.objects.create(
            username="test_user",
            password="12345678910Qaz",
            first_name="Test",
            last_name="User",
            license_number=license_number
        )

        self.assertEqual(dealer.license_number, license_number)

    def test_car_name_str(self) -> None:
        manufacturer = Manufacturer.objects.create(name="Ford", country="USA")

        car = Car.objects.create(model="Focus", manufacturer=manufacturer)

        self.assertEqual(str(car), car.model)
