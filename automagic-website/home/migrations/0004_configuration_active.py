# Generated by Django 4.1.4 on 2023-03-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "home",
            "0003_rename_blog_button_title_configuration_blog_button_text_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="configuration",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]