# Generated by Django 4.1.2 on 2022-11-20 08:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnis', '0018_feedbacks_gallery_events_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacks',
            name='date',
            field=models.DateField(default=datetime.date(2022, 11, 20)),
        ),
    ]
