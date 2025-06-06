import json
import os
import sys
import time
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
                'short_description': raw_place_data.get('description_short', ''),
                'long_description': raw_place_data.get('description_long', ''),
                'latitude': raw_place_data['coordinates']['lat'],
                'longitude': raw_place_data['coordinates']['lng'],
            }
        )

        if not created:
            self.stdout.write(self.style.WARNING(f"Место '{place.title}' уже существует."))
            return

        for idx, img_url in enumerate(raw_place_data.get('imgs', []), start=1):
            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()
            except requests.exceptions.HTTPError as http_err:
                print(f'Ошибка HTTP при загрузке {img_url}: {http_err}', file=sys.stderr)
                continue
            except requests.exceptions.ConnectionError as conn_err:
                print(f'Ошибка соединения при загрузке {img_url}: {conn_err}', file=sys.stderr)
                time.sleep(1)
                continue

            PlaceImage.objects.create(
                place=place,
                position=idx,
                image=ContentFile(
                    img_response.content,
                    name=f'{place.title}_{idx}.jpg',
                ),
            )

        self.stdout.write(self.style.SUCCESS(f'Загружено: {place.title}'))
