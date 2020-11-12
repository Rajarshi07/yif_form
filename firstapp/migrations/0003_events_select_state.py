# Generated by Django 3.0.3 on 2020-08-22 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_registration'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='select_state',
            field=models.CharField(choices=[('West Bengal', 'West bengal'), ('Delhi', 'Delhi'), ('Maharashtra', 'Maharashtra'), ('Odhisha', 'Odhisha'), ('Tamil Nadu', 'Tamil Nadu')], default=1, max_length=50),
        ),
    ]
