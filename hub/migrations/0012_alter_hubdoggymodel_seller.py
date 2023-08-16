# Generated by Django 4.1.2 on 2023-08-16 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hub', '0011_alter_hubdoggymodel_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hubdoggymodel',
            name='seller',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='doggy', to=settings.AUTH_USER_MODEL),
        ),
    ]
