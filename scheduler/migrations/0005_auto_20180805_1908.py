# Generated by Django 2.1 on 2018-08-05 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_remove_bookings_slot_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='client_email',
            field=models.EmailField(max_length=254),
        ),
    ]