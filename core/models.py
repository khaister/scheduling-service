from django.db import models


class PartnerLocation(models.Model):
    class Meta:
        app_label = "core"

    location_id = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10, db_index=True)
