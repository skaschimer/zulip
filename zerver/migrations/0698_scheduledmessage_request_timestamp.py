# Generated by Django 5.1.8 on 2025-04-24 05:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0697_empty_topic_name_for_dms_from_third_party_imports"),
    ]

    operations = [
        migrations.AddField(
            model_name="scheduledmessage",
            name="request_timestamp",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
