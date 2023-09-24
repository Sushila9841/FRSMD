# Generated by Django 4.2.5 on 2023-09-16 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_moodvsfood'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodURLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='food',
            name='url',
        ),
        migrations.AddField(
            model_name='food',
            name='url',
            field=models.ManyToManyField(related_name='foods', to='food.foodurls'),
        ),
    ]
