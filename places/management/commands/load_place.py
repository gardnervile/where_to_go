import json
import os
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from places.models import Place, PlaceImage


class Command(BaseCommand):
    help = 'Загружает место и его фотографии из JSON по URL или локальному пути'

    def add_arguments(self, parser):
        parser.add_argument('source', type=str)

    def handle(self, *args, **options):
        source = options['source']

        if urlparse(source).scheme in ('http', 'https'):
            response = requests.get(source)
            response.raise_for_status()
            raw_place_data = response.json()
        else:
            with open(source, 'r', encoding='utf-8') as f:
                raw_place_data = json.load(f)

        place, created = Place.objects.get_or_create(
            title=raw_place_data['title'],
            defaults={
                'short_description': raw_place_data.get('short_description', ''),
                'long_description': raw_place_data.get('long_description', ''),
                'latitude': raw_place_data['coordinates']['lat'],
                'longitude': raw_place_data['coordinates']['lng'],
            }
        )

        if not created:
            self.stdout.write(self.style.WARNING(f"Место '{place.title}' уже существует."))
            return

        for idx, img_url in enumerate(raw_place_data.get('imgs', []), start=1):
            img_response = requests.get(img_url)
            img_response.raise_for_status()
            img_content = ContentFile(img_response.content)

            image = PlaceImage(place=place, position=idx)
            image.image.save(f'{place.title}_{idx}.jpg', img_content, save=True)

        self.stdout.write(self.style.SUCCESS(f"Загружено: {place.title}"))
