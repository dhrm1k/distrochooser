# Generated by Django 4.2.4 on 2024-08-04 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0116_alter_session_display_mode"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="facetteselectionwidget",
            name="description",
        ),
    ]