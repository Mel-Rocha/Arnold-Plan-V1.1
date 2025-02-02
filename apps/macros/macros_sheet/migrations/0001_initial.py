# Generated by Django 5.0 on 2024-08-10 21:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('macros_planner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MacrosSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.PositiveIntegerField(default=0)),
                ('cho', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('ptn', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('fat', models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('kcal', models.FloatField(default=0)),
                ('macros_planner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='macros_planner.macrosplanner')),
            ],
        ),
    ]
