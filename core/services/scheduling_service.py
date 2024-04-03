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
    location_ids = location_dal.get_location_ids(zip_code)
    if not location_ids:
        _logger.info("Location id not found for zip code %s", zip_code)
        return None

    # get all available appointment times for each location
    _logger.info("Location ids found for zip code %s: %s", zip_code, location_ids)
    appointment_times = []
    for location_id in location_ids:
        next_available = partner_client.get_next_available(location_id)
        if next_available and (time := next_available.get("epoch_time")):
            appointment_times.append({"location_id": location_id, "appointment_time": time})

    if not appointment_times:
        _logger.info("No appointment times found for latitude %s and longitude", latitude, longitude)
        return None

    return sorted(appointment_times, key=lambda x: x["appointment_time"], reverse=True)[0]
