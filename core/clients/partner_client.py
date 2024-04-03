import httpx

from django.conf import settings

URL = settings.PARTNER_API_URL


def get_next_available(location_id) -> dict | None:
    response = httpx.get(f"{URL}/{location_id}")
    if response.status_code != 200:
        return None

    data = response.json()
    return len(data) > 0 and data[0] or None
