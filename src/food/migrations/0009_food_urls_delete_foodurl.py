# Generated by Django 4.2.5 on 2023-09-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0008_remove_food_url_foodurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='urls',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='FoodURL',
        ),
    ]
