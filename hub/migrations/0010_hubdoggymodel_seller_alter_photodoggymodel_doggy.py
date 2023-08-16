# Generated by Django 4.1.2 on 2023-08-16 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('hub', '0009_alter_photodoggymodel_doggy'),
    ]

    operations = [
        migrations.AddField(
            model_name='hubdoggymodel',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to='users.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photodoggymodel',
            name='doggy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='hub.hubdoggymodel'),
        ),
    ]