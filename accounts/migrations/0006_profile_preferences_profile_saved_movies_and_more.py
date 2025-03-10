# Generated by Django 5.1.6 on 2025-03-01 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_delete_newslettersubscription'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='preferences',
            field=models.JSONField(blank=True, default=dict),
        ),
        migrations.AddField(
            model_name='profile',
            name='saved_movies',
            field=models.ManyToManyField(blank=True, related_name='saved_by', to='movies.movie'),
        ),
        migrations.AddField(
            model_name='profile',
            name='watched_movies',
            field=models.ManyToManyField(blank=True, related_name='watched_by', to='movies.movie'),
        ),
    ]
