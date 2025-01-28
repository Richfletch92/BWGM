from django.core.management.base import BaseCommand
from home.models import MovieList, SeriesList


class Command(BaseCommand):
    help = "Clear all data from MovieList and SeriesList models"

    def handle(self, *args, **kwargs):
        MovieList.objects.all().delete()
        SeriesList.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Database cleared successfully!'))
