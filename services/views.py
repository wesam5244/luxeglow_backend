from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse
from django.conf import settings
from .models import Service
from .serializers import ServiceSerializer
import googlemaps

def get_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return JsonResponse(serializer.data, safe=False)

def get_google_reviews(request):
    gmaps = googlemaps.Client(key='AIzaSyAuSIXvsB3p4lmd0IUup8OucuMAvFdbYYU')
    place_name = 'Luxeglow Auto Spa' 
    place_details = gmaps.places(place_name)
    place = gmaps.place(place_details['results'][0]['place_id']) 
    reviews = []
    for review in place['result']['reviews']: 
        print(review)
        reviews.append({
            'name': review['author_name'], 
            'pic': review['profile_photo_url'], 
            'rating': review['rating'], 
            'relative_time_description': review['relative_time_description'], 
            'text': review['text']
        })
    return JsonResponse({'reviews': reviews})