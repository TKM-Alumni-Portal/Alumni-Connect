# Generated by Django 4.1.2 on 2022-11-12 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumnis', '0015_events_mode_events_propic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='proPic',
            new_name='pic',
        ),
    ]
