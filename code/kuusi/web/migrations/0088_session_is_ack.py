# Generated by Django 4.2.4 on 2024-02-04 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0087_session_referrer"),
    ]

    operations = [
        migrations.AddField(
            model_name="session",
            name="is_ack",
            field=models.BooleanField(default=False),
        ),
    ]