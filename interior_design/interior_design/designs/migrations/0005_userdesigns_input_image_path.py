# Generated by Django 4.2.3 on 2025-04-05 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("designs", "0004_alter_userdesigns_promote"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdesigns",
            name="input_image_path",
            field=models.CharField(blank=True, default="", max_length=500),
        ),
    ]
