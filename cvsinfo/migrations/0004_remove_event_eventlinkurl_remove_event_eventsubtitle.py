# Generated by Django 4.1.3 on 2022-11-21 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cvsinfo', '0003_event_eventcompany'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='eventLinkURL',
        ),
        migrations.RemoveField(
            model_name='event',
            name='eventSubtitle',
        ),
    ]
