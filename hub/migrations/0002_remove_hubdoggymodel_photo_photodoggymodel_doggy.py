# Generated by Django 4.1.2 on 2023-08-04 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hubdoggymodel',
            name='photo',
        ),
        migrations.AddField(
            model_name='photodoggymodel',
            name='doggy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hub.hubdoggymodel'),
        ),
    ]
