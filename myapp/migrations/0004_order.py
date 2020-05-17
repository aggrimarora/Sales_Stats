# Generated by Django 3.0.6 on 2020-05-15 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200515_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('Total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('ProductID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.Product')),
                ('RepID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.SalesRep')),
            ],
        ),
    ]