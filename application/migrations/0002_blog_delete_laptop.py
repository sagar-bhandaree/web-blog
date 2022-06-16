# Generated by Django 4.0.1 on 2022-01-28 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("title", models.CharField(max_length=10)),
                ("desc", models.CharField(max_length=100)),
                ("thumbnail", models.URLField()),
                ("read_more", models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name="Laptop",
        ),
    ]
