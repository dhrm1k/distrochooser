# Generated by Django 4.2.4 on 2023-11-25 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0083_facetteradioselectionwidget"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="facetteassignment",
            name="description",
        ),
    ]