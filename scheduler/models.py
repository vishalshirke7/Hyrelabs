from django.db import models

# Create your models here.


class User(models.Model):

    user_fname = models.CharField(max_length=80)
    user_lname = models.CharField(max_length=80)
    user_email = models.EmailField(unique=True)
    # user_isactive = models.BooleanField()
    user_password = models.CharField(max_length=500)
    # user_verf_link =  models.CharField(max_length=100,default="null")
    def user_mail(self):
        return self.user_email


class Bookings(models.Model):

    client_name = models.CharField(max_length=20)
    client_email = models.EmailField()
    slot_date = models.CharField(max_length=20)
    slot_time = models.CharField(max_length=20)
    slot_end_time = models.CharField(max_length=20)
    is_scheduled = models.BooleanField(default=False)
