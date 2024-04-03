import logging

from core.clients import zip_code_client, partner_client
from core.data_access import location_dal

_logger = logging.getLogger(__name__)


def get_next_available_appointment(latitude, longitude) -> dict | None:
    if not latitude or not longitude:
        raise ValueError("Latitude and longitude are required")

    # translate latitude and longitude to zip code
    zip_code = zip_code_client.get_zip_code(latitude, longitude)
    if not zip_code:
        _logger.info(
            "Zip code not found for latitude %s and longitude %s", latitude, longitude
        )
        return None

    # translate zip code to location id
    location_id = location_dal.get_location_id(zip_code)
    if not location_id:
        _logger.info("Location id not found for zip code %s", zip_code)
        return None

    return partner_client.get_next_available(location_id)
