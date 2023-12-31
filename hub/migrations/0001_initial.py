# Generated by Django 4.1.2 on 2023-08-04 10:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoDoggyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='uploads/DoggyPhoto')),
            ],
        ),
        migrations.CreateModel(
            name='HubDoggyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age_old', models.IntegerField(validators=[django.core.validators.MaxValueValidator(22)])),
                ('months_old', models.IntegerField(validators=[django.core.validators.MaxValueValidator(12)])),
                ('gender', models.CharField(choices=[('Boy', 'Boy'), ('Girl', 'Girl')], default='Boy', max_length=4)),
                ('place', models.CharField(max_length=255)),
                ('slug', models.SlugField(default='')),
                ('photo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hub.photodoggymodel')),
            ],
        ),
    ]
