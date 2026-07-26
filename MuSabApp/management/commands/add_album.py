from django.core.management.base import BaseCommand
from MuSabApp.models import Album


class Command(BaseCommand):
    help = "Add a single album"

    def add_arguments(self, parser):
        parser.add_argument("--year", type=int, required=True)
        parser.add_argument("--artist", type=str, required=True)
        parser.add_argument("--album", type=str, required=True)
        parser.add_argument("--genre", type=str, required=True)
        parser.add_argument("--rating", type=float, required=True)
        parser.add_argument("--cover", type=str, required=True)

    def handle(self, *args, **kwargs):
        album, created = Album.objects.get_or_create(
            artist=kwargs["artist"],
            album=kwargs["album"],
            defaults={
                "year": kwargs["year"],
                "genre": kwargs["genre"],
                "rating": kwargs["rating"],
                "cover": kwargs["cover"],
            }
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Added: {album.artist} - {album.album}"
                )
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f"Already exists: {album.artist} - {album.album}"
                )
            )