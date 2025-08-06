from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Optional: Clear existing data
        Listing.objects.all().delete()

        self.stdout.write('Creating sample listings...')

        for _ in range(10):  # Adjust number as needed
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(nb_sentences=3),
                price=round(random.uniform(100.0, 10000.0), 2),
                location=fake.city()
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded listings.'))
