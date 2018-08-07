from django.urls import path

from . import views

app_name = 'scheduler'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('bookslot/', views.book_slot, name='book_slot'),
    path('logout/', views.logout, name='logout'),
    path('createevent/', views.create_event, name='create_event')
]