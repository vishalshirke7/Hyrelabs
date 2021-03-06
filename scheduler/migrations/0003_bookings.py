# Generated by Django 2.1 on 2018-08-05 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0002_auto_20180804_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_email', models.EmailField(max_length=254, unique=True)),
                ('slot_date', models.DateField()),
                ('slot_time', models.TimeField()),
            ],
        ),
    ]
