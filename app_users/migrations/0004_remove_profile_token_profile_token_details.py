# Generated by Django 5.0.7 on 2024-07-31 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='token',
        ),
        migrations.AddField(
            model_name='profile',
            name='token_details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
