# Generated by Django 5.1.3 on 2024-11-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backend", "0002_rename_user_name_m_user_full_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="restaurant_address",
            field=models.CharField(default="null", max_length=255),
        ),
        migrations.AddField(
            model_name="restaurant",
            name="restaurant_desc",
            field=models.CharField(default="null", max_length=255),
        ),
    ]
