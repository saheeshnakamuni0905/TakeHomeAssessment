from django.test import TestCase
from .models import Company, Location

class CompanyModelTest(TestCase):

    def setUp(self):
        self.company = Company.objects.create(
            company_id=1,
            name="TechNova Solutions",
            address="123 Innovation Drive, San Francisco, CA 94105",
            latitude=37.7749,
            longitude=-122.4194
        )

    def test_company_creation(self):
        self.assertEqual(self.company.name, "TechNova Solutions")
        self.assertEqual(self.company.address, "123 Innovation Drive, San Francisco, CA 94105")
        self.assertEqual(self.company.latitude, 37.7749)
        self.assertEqual(self.company.longitude, -122.4194)

class LocationModelTest(TestCase):

    def setUp(self):
        self.company = Company.objects.create(
            company_id=1,
            name="TechNova Solutions",
            address="123 Innovation Drive, San Francisco, CA 94105",
            latitude=37.7749,
            longitude=-122.4194
        )
        self.location = Location.objects.create(
            location_id=1,
            company=self.company,
            name="TechNova HQ",
            address="123 Innovation Drive, San Francisco, CA 94105",
            latitude=37.7749,
            longitude=-122.4194
        )

    def test_location_creation(self):
        self.assertEqual(self.location.name, "TechNova HQ")
        self.assertEqual(self.location.address, "123 Innovation Drive, San Francisco, CA 94105")
        self.assertEqual(self.location.latitude, 37.7749)
        self.assertEqual(self.location.longitude, -122.4194)
        self.assertEqual(self.location.company, self.company)
