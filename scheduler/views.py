import datetime
from datetime import timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.urls import reverse
from django import forms

import pytz
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

from .forms import SignupForm, LoginForm
from .models import User, Bookings

SCOPES = 'https://www.googleapis.com/auth/calendar'


def index(request):
    if 'user_id' in request.session:
        userid = request.session['user_id']
        user = User.objects.get(pk=userid)
        booking = Bookings.objects.all()
        return render(request, 'scheduler/availableslots.html', {'user': user, 'booking': booking})
    else:
        return render(request, 'scheduler/home.html')


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = User()
            user.user_fname = form.cleaned_data['fname'].strip()
            user.user_lname = form.cleaned_data['lname'].strip()
            user.user_email = form.cleaned_data['email'].strip()
            user.user_password = form.cleaned_data['password'].strip()
            user.save()
            return HttpResponseRedirect(reverse('scheduler:login'))
    elif 'user_id' in request.session:
        return HttpResponseRedirect(reverse('scheduler:index'))
    else:
        form = SignupForm()

    return render(request, 'scheduler/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(user_email=request.POST['username'])
            request.session['user_id'] = user.id
            return HttpResponseRedirect(reverse('scheduler:index'))
    elif 'user_id' in request.session:
        return HttpResponseRedirect(reverse('scheduler:index'))
    else:
        form = LoginForm()
    return render(request, 'scheduler/login.html', {'form': form})


def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('scheduler:index'))


def book_slot(request):
    if request.method == 'POST':
        time = request.POST.get('drpdwntime')
        date = request.POST.get('drpdwndate')
        print(time)
        userid = request.session['user_id']
        user = User.objects.get(pk=userid)
        usermail = user.user_email
        username= user.user_fname
        try:
            booking = Bookings.objects.get(client_email=usermail)
        except Bookings.DoesNotExist:
            bookings = Bookings()
            bookings.client_email = usermail
            bookings.client_name = username
            ls = time.split("-")
            bookings.slot_time = ls[0]
            bookings.slot_date = date

            bookings.slot_end_time = ls[1]
            bookings.save()
            return render(request, 'scheduler/abc.html', {'bookings': bookings})
        return render(request, 'scheduler/abc.html', {'booking': booking})
    else:
        return HttpResponseRedirect(reverse('scheduler:index'))


def create_event(request):

    if request.method == 'POST':
    # print(request.POST.get('abc@gmail.com'))
        clientname = request.POST.get('drpdwndate')
        if request.POST.get('accept'):

            booking = Bookings.objects.get(client_email=clientname)
            date = booking.slot_date
            start_time = booking.slot_time
            end_time = booking.slot_end_time
            booking.is_scheduled = True
            booking.save()
            # userid = request.session['user_id']
            # user = User.objects.get(pk=userid)
            service = create_service()
            # start_datetime = datetime.datetime.now(tz=pytz.utc)
            f = "%Y-%m-%d %H:%M"
            startdatestring1 = date + " " + start_time
            startdatestring2 = date + " " + end_time
            sf_timezone = pytz.timezone('Asia/Kolkata')

            start_datetime = datetime.datetime.strptime(startdatestring1, f).astimezone(sf_timezone)
            end_datetime = datetime.datetime.strptime(startdatestring2, f).astimezone(sf_timezone)
            event = service.events().insert(calendarId='primary', body={
                'summary': 'Meeting with ' + booking.client_name,
                'description': 'Created using scheduler app',
                'start': {'dateTime': (start_datetime+timedelta(hours=12)).isoformat()},
                'end': {'dateTime': (end_datetime+timedelta(hours=12)).isoformat()},
            }).execute()
            return render(request, 'scheduler/successfulschedule.html', {'booking': booking})
        elif request.POST.get('reject'):
            booking = Bookings.objects.get(client_email=clientname)
            booking.delete()
            return render(request, 'scheduler/successfulschedule.html', {'clientname': clientname})
    else:
        return HttpResponseRedirect(reverse('scheduler:index'))


# def cancel_appointment(request):
#     if request.method == 'POST':
#     # print(request.POST.get('abc@gmail.com'))
#         clientname = request.POST.get('drpdwndate')
#         booking = Bookings.objects.get(client_email=clientname)
#         booking.delete()
#         return render(request, 'scheduler/successfulschedule.html', {'clientname': clientname})
#     else:
#         return HttpResponseRedirect(reverse('scheduler:index'))


def create_service():
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    return service