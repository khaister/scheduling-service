from decimal import Decimal

from django.conf import settings
import httpx

GOOGLE_REVERSE_GEOCODING_API_KEY = settings.GOOGLE_REVERSE_GEOCODING_API_KEY
GOOGLE_REVERSE_GEOCODING_URL = "https://maps.googleapis.com/maps/api/geocode/json"


def get_zip_code(latitude: Decimal, longitude: Decimal) -> str | None:
    params = {
        "latlng": f"{latitude},{longitude}",
        "result_type": "postal_code",
        "key": GOOGLE_REVERSE_GEOCODING_API_KEY,
    }
    response = httpx.get(GOOGLE_REVERSE_GEOCODING_URL, params=params)
    if response.status_code != 200:
        return None

    data = response.json() or {}
    if data.get("status") != "OK":
        return None

    results = data.get("results", [])
    address_components = len(results) > 0 and results[0].get("address_components", [])
    zip_code = next((item.get("short_name") for item in address_components if "postal_code" in item.get("types", [])), None)
    return zip_code
