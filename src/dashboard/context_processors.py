import json
from django.utils import timezone

from dashboard.models import Site
import requests


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def location_processor(request):
    client_ip = get_client_ip(request)
    location_data = {
        'city': '',
        'region': '',
        'country': 'USA'
    }
    try:
        response = requests.get(f'http://www.geoplugin.net/json.gp?ip={client_ip}')
        response.raise_for_status()
        data = response.json()
        location_data = {
            'city': data.get('city', ''),
            'region': data.get('region', ''),
            'country': data.get('country_name', 'USA')  # Use 'USA' as default if not provided
        }
        print("Location data:", location_data)  # Print location data for debugging
    except requests.RequestException as e:
        print("Error fetching location data:", e)  # Print error for debugging

    return {'location': location_data}

def site_processor(request):
    site_instance = Site.objects.first()
    site_data = SiteSerializer(site_instance).data if site_instance else None
    return {
        'site': site_instance,
        'site_json': json.dumps(site_data),
    }
