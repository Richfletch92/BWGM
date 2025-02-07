from django.core.management.base import BaseCommand
from home.models import MovieList, SeriesList


class Command(BaseCommand):
    help = "Clear all data from MovieList and SeriesList models"

    def handle(self, *args, **kwargs):
        # Delete all records from MovieList model
        MovieList.objects.all().delete()
        # Delete all records from SeriesList model
        SeriesList.objects.all().delete()
        # Print success message to the console
        self.stdout.write(self.style.SUCCESS('Database cleared successfully!'))
