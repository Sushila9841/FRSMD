# Generated by Django 4.2.5 on 2023-09-13 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0002_moodhistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='has_filled_survey',
            field=models.BooleanField(default=False),
        ),
    ]