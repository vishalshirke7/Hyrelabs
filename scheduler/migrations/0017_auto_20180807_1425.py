# Generated by Django 2.1 on 2018-08-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0016_auto_20180807_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='is_scheduled',
            field=models.BooleanField(default=False),
        ),
    ]