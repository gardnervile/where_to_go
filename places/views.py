from django.shortcuts import render
from .models import Place
import json

def show_places(request):
    places = Place.objects.all()
    
    places_data = []
    for place in places:
        places_data.append({
            'name': place.name,
            'latitude': place.latitude,
            'longitude': place.longitude,
            'image_url': place.image.url,
        })
    
    return render(request, 'index.html', {'places_data': json.dumps(places_data)})

