# Generated by Django 2.2.4 on 2019-10-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_auto_20191020_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='transport_needed',
            field=models.CharField(choices=[(None, '-- Select Option --'), ('drive', 'Driving'), ('th-bus', 'TAMUhack Bus'), ('fly', 'Flying'), ('public', 'Public Transportation'), ('walk-cycle', 'Walking/Biking')], max_length=11, verbose_name='How will you be getting to the event?'),
        ),
    ]