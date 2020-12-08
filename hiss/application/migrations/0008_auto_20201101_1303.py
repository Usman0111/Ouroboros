# Generated by Django 2.2.13 on 2020-11-01 19:03

import django.core.validators
import django_s3_storage.storage
from django.db import migrations, models

import application.filesize_validation
import application.models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0007_auto_20200809_1434"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="hackathon_purpose",
            field=models.CharField(
                choices=[
                    ("W", "I want to win!"),
                    ("L", "I want to learn something new!"),
                    ("WR", "I just want to attend all the workshops"),
                    (
                        "R",
                        "I literally signed up to talk to the awesome sponsors and get a job",
                    ),
                    ("M", "I want to just mess around on the Minecraft server!"),
                ],
                default="R",
                max_length=16,
                verbose_name="What is your main purpose for registering for this event?",
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="has_team",
            field=models.BooleanField(
                default=True, verbose_name="I have a team already"
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="wants_team",
            field=models.BooleanField(
                default=False,
                help_text="We will take into account many factors to make sure you are paired with a team that works well.",
                verbose_name="I would like to be paired with a hand-crafted team",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="grad_year",
            field=models.IntegerField(
                choices=[
                    (2020, 2020),
                    (2021, 2021),
                    (2022, 2022),
                    (2023, 2023),
                    (2024, 2024),
                ],
                verbose_name="What is your anticipated graduation year?",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="question3",
            field=models.TextField(
                max_length=500,
                verbose_name="What is a cool prize you'd like to win at TAMUhack?",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="resume",
            field=models.FileField(
                help_text="Companies will use this resume to offer interviews for internships and full-time positions.",
                storage=django_s3_storage.storage.S3Storage(),
                upload_to=application.models.uuid_generator,
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["pdf"]
                    ),
                    application.filesize_validation.FileSizeValidator(max_filesize=2.5),
                ],
                verbose_name="Upload your resume (PDF only)",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="transport_needed",
            field=models.CharField(
                choices=[
                    ("D", "Driving"),
                    ("B", "TAMUhack Bus"),
                    ("BUT", "TAMUhack Bus - UT Austin"),
                    ("BUTD", "TAMUhack Bus - UT Dallas"),
                    ("BUTA", "TAMUhack Bus - UT Arlington"),
                    ("BUTSA", "TAMUhack Bus - UTSA"),
                    ("BUTRGV", "TAMUhack Bus - UTRGV"),
                    ("OB", "Other Bus (Greyhound, Megabus, etc.)"),
                    ("F", "Flying"),
                    ("P", "Public Transportation"),
                    ("M", "Walking/Biking"),
                ],
                max_length=11,
                verbose_name="How will you be getting to the event?",
            ),
        ),
    ]
