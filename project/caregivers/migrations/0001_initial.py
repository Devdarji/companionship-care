# Generated by Django 4.0.1 on 2022-07-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Caregiver",
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
                ("display_name", models.CharField(max_length=255)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("INDIVIDUAL", "Individual"),
                            ("ORGANIZATION", "Organization"),
                        ],
                        default="INDIVIDUAL",
                        max_length=15,
                    ),
                ),
            ],
        )
    ]
