# Generated by Django 5.0.2 on 2024-02-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app_list", "0002_academy"),
    ]

    operations = [
        migrations.CreateModel(
            name="Programation",
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
                ("nome", models.CharField(max_length=100, verbose_name="nome")),
            ],
        ),
    ]