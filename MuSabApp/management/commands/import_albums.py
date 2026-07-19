from django.core.management.base import BaseCommand
import pandas as pd
from MuSabApp.models import Album

class Command(BaseCommand):
    help = 'Import albums from CSV'

    def handle(self, *args, **kwargs):
        df = pd.read_csv('data/albums.csv')

        for _, row in df.iterrows():
            Album.objects.create(
                year=row['year'],
                artist=row['artist'],
                album=row['album'],
                genre=row['genre'],
                rating=row['rating']
            )

        self.stdout.write(
            self.style.SUCCESS('Successfully imported albums from CSV')
        )
