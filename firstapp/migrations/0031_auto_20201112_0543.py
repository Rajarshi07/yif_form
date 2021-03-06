# Generated by Django 3.0.3 on 2020-11-12 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0030_auto_20201028_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='eventadmin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='events',
            name='start_day',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='registration',
            name='day_registered',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
