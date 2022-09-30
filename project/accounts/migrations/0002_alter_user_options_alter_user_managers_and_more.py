# Generated by Django 4.0 on 2022-01-04 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(name="user", options={}),
        migrations.AlterModelManagers(name="user", managers=[]),
        migrations.RemoveField(model_name="user", name="date_joined"),
        migrations.RemoveField(model_name="user", name="first_name"),
        migrations.RemoveField(model_name="user", name="is_active"),
        migrations.RemoveField(model_name="user", name="is_staff"),
        migrations.RemoveField(model_name="user", name="last_name"),
        migrations.RemoveField(model_name="user", name="username"),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, unique=True, verbose_name="email address"
            ),
        ),
    ]
