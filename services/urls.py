from django.urls import path
from .views import get_services, get_google_reviews

urlpatterns = [
    path('services/', get_services, name='get_services'),
    path('reviews/', get_google_reviews, name='get_google_reviews'),
]