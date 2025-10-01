from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing, Booking
from faker import Faker
import random
from datetime import datetime, timedelta

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample listings and bookings'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=10, help='Number of listings to create')

    def handle(self, *args, **options):
        fake = Faker()
        count = options['count']
        
        # Create a superuser if it doesn't exist
        if not User.objects.filter(is_superuser=True).exists():
            admin = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('Created admin user'))
        else:
            admin = User.objects.filter(is_superuser=True).first()

        # Create some regular users
        num_users = 5
        for i in range(num_users):
            username = f'user{i+1}'
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username,
                    email=f'{username}@example.com',
                    password='password123'
                )
        users = list(User.objects.all())
        
        self.stdout.write(f'Creating {count} sample listings...')
        
        # Create listings
        listings = []
        for i in range(count):
            listing = Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=5),
                price=random.randint(50, 500),
            )
            listings.append(listing)
            
            # Create some bookings for each listing
            num_bookings = random.randint(1, 5)
            for _ in range(num_bookings):
                user = random.choice(users)
                start_date = fake.date_between(start_date='-30d', end_date='+30d')
                end_date = start_date + timedelta(days=random.randint(1, 14))
                
                Booking.objects.create(
                    user=user,
                    listing=listing,
                    check_in=start_date,
                    check_out=end_date
                )
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} listings with random bookings!'))
