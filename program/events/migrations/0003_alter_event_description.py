# Generated by Django 5.0 on 2024-01-03 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_rename_name_event_title_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default='Please input the information for this event.'),
        ),
    ]
