# Generated by Django 4.2.3 on 2025-04-05 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("designs", "0003_userdesigns_delete_userdesign"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userdesigns",
            name="promote",
            field=models.CharField(max_length=500),
        ),
    ]
