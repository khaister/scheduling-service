from core.models import PartnerLocation


def get_location_ids(zip_code: str) -> list[str] | None:
    return PartnerLocation.objects.filter(zip_code=zip_code).values_list(
        "location_id", flat=True
    )
