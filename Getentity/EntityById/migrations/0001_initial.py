# Generated by Django 5.0.6 on 2024-05-29 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="FDB_entities",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("category", models.CharField(blank=True, max_length=255, null=True)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "natural_source",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
            options={
                "db_table": "fdb_entities",
            },
        ),
    ]
