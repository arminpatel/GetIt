# Generated by Django 4.2 on 2023-12-28 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='cover_image',
        ),
    ]
