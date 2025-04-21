from django.shortcuts import render, get_object_or_404
from .models import Place
import json
from django.http import JsonResponse

def show_places(request):
    places = Place.objects.all()

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in places:
        geojson["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": f"place_{place.id}",
                "detailsUrl": f"/static/places/{place.id}.json"  # заглушка
            }
        })

    return render(request, 'index.html', {
        'geojson_data': json.dumps(geojson, ensure_ascii=False)
    })

def place_detail(request, id):
    place = get_object_or_404(Place, id=id)

    images = [img.image.url for img in place.images.all()]

    data = {
        "title": place.title,
        "imgs": images,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.latitude,
            "lng": place.longitude,
        }
    }

    return JsonResponse(
        data,
        json_dumps_params={'ensure_ascii': False, 'indent': 2},
        content_type='application/json; charset=utf-8'
    )