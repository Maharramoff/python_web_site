# Generated by Django 2.2.7 on 2020-04-07 23:00

from django.db import migrations, models
import seminars.models


class Migration(migrations.Migration):

    dependencies = [
        ('seminars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seminar',
            name='seminar_photo',
            field=models.ImageField(blank=True, default='', null=True, upload_to=seminars.models.upload_to),
        ),
    ]
