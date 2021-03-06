# Generated by Django 3.0.3 on 2020-10-28 20:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0029_auto_20201028_0429'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='registration_data',
            field=models.FileField(default='', upload_to='reg_data'),
        ),
        migrations.AlterField(
            model_name='events',
            name='cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='events',
            name='rules',
            field=models.TextField(default='', max_length=1500),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_day',
            field=models.DateField(default=datetime.datetime(2020, 10, 28, 20, 6, 20, 80658)),
        ),
        migrations.AlterField(
            model_name='registration',
            name='day_registered',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 10, 28, 20, 6, 20, 97811)),
        ),
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 10, 28, 20, 6, 20, 97746, tzinfo=utc)),
        ),
    ]
