# Generated by Django 2.1 on 2018-08-06 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_auto_20180805_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='slot_time',
            field=models.CharField(max_length=100),
        ),
    ]