# Generated by Django 2.2.13 on 2020-11-01 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0008_auto_20201101_1303"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="technology_experience",
            field=models.CharField(default=None, max_length=150),
        ),
    ]
