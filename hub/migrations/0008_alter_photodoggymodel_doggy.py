# Generated by Django 4.1.2 on 2023-08-14 10:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0007_hubdoggymodel_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photodoggymodel',
            name='doggy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hub.hubdoggymodel'),
        ),
    ]
