# Generated by Django 2.2.3 on 2022-11-10 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnis', '0013_auto_20221110_0804'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]
