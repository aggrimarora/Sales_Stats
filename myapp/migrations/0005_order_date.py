# Generated by Django 3.0.6 on 2020-05-15 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 15, 18, 5, 26, 350417)),
        ),
    ]