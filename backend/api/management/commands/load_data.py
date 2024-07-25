# backend/api/management/commands/load_data.py

import csv
from django.core.management.base import BaseCommand
from api.models import Company, Location

class Command(BaseCommand):
    help = 'Load data from CSV files'

    def handle(self, *args, **kwargs):
        with open('../csv/companies.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Company.objects.create(
                    company_id=row['company_id'],
                    name=row['name'],
                    address=row['address'],
                    latitude=row['latitude'],
                    longitude=row['longitude']
                )

        with open('../csv/locations.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                company = Company.objects.get(company_id=row['company_id'])
                Location.objects.create(
                    location_id=row['location_id'],
                    company=company,
                    name=row['name'],
                    address=row['address'],
                    latitude=row['latitude'],
                    longitude=row['longitude']
                )
