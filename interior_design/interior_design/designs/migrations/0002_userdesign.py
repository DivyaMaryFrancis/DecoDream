# Generated by Django 4.2.3 on 2025-02-13 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("designs", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserDesign",
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
                ("design_name", models.CharField(max_length=255, unique=True)),
                ("image_path", models.CharField(max_length=500)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="designs.registeruser",
                    ),
                ),
            ],
        ),
    ]
