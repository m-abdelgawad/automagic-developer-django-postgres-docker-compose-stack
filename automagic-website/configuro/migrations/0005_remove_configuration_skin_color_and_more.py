# Generated by Django 4.1.4 on 2023-05-04 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("configuro", "0004_configuration_skin_color_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="configuration",
            name="skin_color",
        ),
        migrations.RemoveField(
            model_name="configuration",
            name="skin_color_dark",
        ),
        migrations.RemoveField(
            model_name="configuration",
            name="skin_color_light",
        ),
    ]