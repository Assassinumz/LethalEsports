# Generated by Django 4.1.2 on 2022-12-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='#', max_length=600)),
                ('image', models.URLField(default='https://as2.ftcdn.net/v2/jpg/03/95/37/19/1000_F_395371923_x2IUqSOYDCQeBCx3auKcK3EbyzNjhlNV.jpg')),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='null', max_length=100)),
                ('last_name', models.CharField(default='null', max_length=100)),
                ('ign', models.CharField(default='null', max_length=60)),
                ('doj', models.DateField()),
                ('image', models.CharField(default='#', max_length=600)),
                ('description', models.TextField(default='#')),
                ('platform', models.TextField(blank=True, choices=[('youtube', 'youtube'), ('twitch', 'twitch')], default='youtube')),
                ('streams', models.TextField(blank=True, null=True)),
                ('instagram_followers', models.CharField(blank=True, max_length=60, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=600, null=True)),
                ('youtube_subs', models.CharField(blank=True, max_length=60, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=600, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='#', max_length=600)),
                ('location', models.CharField(default='Online', max_length=100)),
                ('image', models.CharField(default='#', max_length=600)),
                ('link', models.CharField(blank=True, default='#', max_length=600)),
                ('description', models.TextField(default='#')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='null', max_length=100)),
                ('last_name', models.CharField(default='null', max_length=100)),
                ('ign', models.CharField(default='null', max_length=60)),
                ('doj', models.DateField()),
                ('image', models.CharField(default='#', max_length=600)),
                ('description', models.TextField(default='#')),
                ('instagram_followers', models.CharField(blank=True, max_length=60, null=True)),
                ('instagram_link', models.CharField(max_length=600, null=True)),
                ('youtube_subs', models.CharField(blank=True, max_length=60, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=600, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='null', max_length=100)),
                ('last_name', models.CharField(default='null', max_length=100)),
                ('ign', models.CharField(default='null', max_length=60)),
                ('doj', models.DateField()),
                ('image', models.CharField(default='#', max_length=600)),
                ('description', models.TextField(default='#')),
                ('game', models.TextField(blank=True, choices=[('valorant', 'Valorant'), ('csgo', 'CSGO')], default='valorant')),
                ('streams', models.TextField(blank=True, null=True)),
                ('instagram_followers', models.CharField(blank=True, max_length=60, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=600, null=True)),
                ('youtube_subs', models.CharField(blank=True, max_length=60, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=600, null=True)),
            ],
        ),
    ]
