# Generated by Django 5.0.3 on 2024-04-03 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PartnerLocation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location_id", models.CharField(max_length=10)),
                ("zip_code", models.CharField(db_index=True, max_length=10)),
            ],
        ),
    ]