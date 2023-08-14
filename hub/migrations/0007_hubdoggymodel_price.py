# Generated by Django 4.1.2 on 2023-08-11 05:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0006_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='hubdoggymodel',
            name='price',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
