# Generated by Django 5.0.7 on 2024-08-01 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0004_remove_profile_token_profile_token_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='provider',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]