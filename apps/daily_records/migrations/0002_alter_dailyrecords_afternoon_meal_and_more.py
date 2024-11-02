# Generated by Django 5.0 on 2024-08-17 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daily_records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyrecords',
            name='afternoon_meal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dailyrecords',
            name='evening_meal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='dailyrecords',
            name='morning_meal',
            field=models.BooleanField(default=False),
        ),
    ]
