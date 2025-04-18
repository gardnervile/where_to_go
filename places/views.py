from django.shortcuts import render
from .models import Place
import json

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
