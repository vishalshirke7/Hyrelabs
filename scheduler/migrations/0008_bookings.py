# Generated by Django 2.1 on 2018-08-06 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_delete_bookings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=20)),
                ('client_email', models.EmailField(max_length=254)),
                ('slot_date', models.CharField(max_length=100)),
                ('slot_time', models.CharField(max_length=100)),
            ],
        ),
    ]
