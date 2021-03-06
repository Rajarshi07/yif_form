# Generated by Django 3.0.3 on 2020-09-16 15:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0021_auto_20200916_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='group_event',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_day',
            field=models.DateField(default=datetime.datetime(2020, 9, 9, 20, 55, 5, 901924)),
        ),
        migrations.AlterField(
            model_name='registration',
            name='day_registered',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 9, 16, 20, 55, 6, 505878)),
        ),
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 16, 15, 25, 6, 505878, tzinfo=utc)),
        ),
    ]
