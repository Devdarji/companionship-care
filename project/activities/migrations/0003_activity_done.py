# Generated by Django 4.0.1 on 2022-03-29 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0002_activity_note"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="done",
            field=models.BooleanField(default=False),
        ),
    ]
