# Generated by Django 4.1.2 on 2023-01-02 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_player_twitter_followers_player_twitter_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='management',
            name='role',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
