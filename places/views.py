import json

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from .models import Place


def show_places(request):
    places = Place.objects.all()

    features = [
        {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'short_description': place.short_description,
                'placeId': f'place_{place.id}',
                'detailsUrl': reverse('place_detail', args=[place.id]),
            }
        }
        for place in places
    ]

    geojson = {
        'type': 'FeatureCollection',
        'features': features,
    }

    return render(request, 'index.html', {
        'geojson_data': json.dumps(geojson, ensure_ascii=False)
    })


def place_detail(request, id):
    place = get_object_or_404(
        Place.objects.prefetch_related('images'),
        id=id
    )

    images = [img.image.url for img in place.images.all()]

    serialized_place = {
        'title': place.title,
        'imgs': images,
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude,
        }
    }

    return JsonResponse(
        serialized_place,
        json_dumps_params={'ensure_ascii': False, 'indent': 2},
        content_type='application/json; charset=utf-8'
    )
