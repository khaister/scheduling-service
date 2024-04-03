import logging

from core.clients import geocoding_client, partner_client
from core.data_access import location_dal

_logger = logging.getLogger(__name__)


def get_next_available_appointment(latitude, longitude) -> dict | None:
    if not latitude or not longitude:
        raise ValueError("Latitude and longitude are required")

    # given lat and long, call google geocoding api to get zip
    # return none if zip is not found
    zip_code = geocoding_client.get_zip_code(latitude, longitude)
    if not zip_code:
        _logger.info(
            "Zip code not found for latitude %s and longitude %s", latitude, longitude
        )
        return None

    # if zip is found, call data access to get location id
    # return none if location id is not found
    # todo: try..catch here
    location_id = location_dal.get_location_id(zip_code)
    if not location_id:
        _logger.info("Location id not found for zip code %s", zip_code)
        return None

    # if location id is found, call solv next-available api to get appointment
    # todo: try..catch here
    return partner_client.get_next_available(location_id)
