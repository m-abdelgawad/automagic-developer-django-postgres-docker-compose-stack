# Generated by Django 4.1.4 on 2023-05-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CounterUpItem",
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
                ("title", models.CharField(max_length=250)),
                ("count_number", models.CharField(max_length=250)),
                ("icon", models.CharField(max_length=250)),
                ("order", models.PositiveIntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[("DF", "Draft"), ("PB", "Published")],
                        default="DF",
                        max_length=2,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SliderShowcaseApp",
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
                ("title", models.CharField(max_length=250)),
                ("short_description", models.TextField()),
                ("long_description", models.TextField()),
                ("button_text", models.CharField(max_length=250)),
                ("button_icon", models.CharField(max_length=250)),
                ("button_url", models.CharField(max_length=500)),
                ("image", models.ImageField(upload_to="app_image")),
                ("order", models.PositiveIntegerField()),
                (
                    "status",
                    models.CharField(
                        choices=[("DF", "Draft"), ("PB", "Published")],
                        default="DF",
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]