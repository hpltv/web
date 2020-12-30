# Generated by Django 3.1.4 on 2020-12-31 19:02

from django.db import migrations, models

import hijaponmelatele.web.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TVEntry",
            fields=[
                (
                    "id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                ("title", models.CharField(db_index=True, max_length=100, unique=True)),
                ("url", models.URLField(db_index=True)),
                ("image_url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="DisplayConfig",
            fields=[
                (
                    "id",
                    models.AutoField(editable=False, primary_key=True, serialize=False),
                ),
                (
                    "public_name",
                    models.CharField(db_index=True, max_length=100, unique=True),
                ),
                (
                    "private_id",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        default=hijaponmelatele.web.models.create_id,
                        editable=False,
                        max_length=64,
                        unique=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "entries",
                    models.ManyToManyField(related_name="configs", to="web.TVEntry"),
                ),
            ],
        ),
    ]