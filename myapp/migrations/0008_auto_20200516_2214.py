# Generated by Django 3.0.6 on 2020-05-16 22:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200516_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 16, 22, 14, 41, 200631)),
        ),
    ]