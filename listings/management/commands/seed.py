# listings/management/commands/seed.py
from django.core.management.base import BaseCommand
from listings.models import Listing
from django.utils import timezone
import random

SAMPLE_LISTINGS = [
    {
        'title': 'Seaside Studio',
        'description': 'Cozy studio by the sea, walking distance to the beach.',
        'location': 'Mombasa, Kenya',
        'price_per_night': '25.00',
    },
    {
        'title': 'City Apartment',
        'description': 'Central apartment with fast wifi and workspace.',
        'location': 'Nairobi, Kenya',
        'price_per_night': '40.00',
    },
    {
        'title': 'Countryside Cottage',
        'description': 'Quiet cottage with garden and fireplace.',
        'location': 'Narok, Kenya',
        'price_per_night': '30.00',
    },
]

class Command(BaseCommand):
    help = "Seed the database with sample listings."

    def handle(self, *args, **options):
        created = 0
        for item in SAMPLE_LISTINGS:
            obj, was_created = Listing.objects.get_or_create(
                title=item['title'],
                defaults={
                    'description': item['description'],
                    'location': item['location'],
                    'price_per_night': item['price_per_night'],
                    'created_at': timezone.now(),
                }
            )
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Seed complete. Created {created} listings."))
