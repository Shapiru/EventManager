from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='Fire'

urlpatterns=[
    path('', views.index, name='index'),
    path('(?P<event_id>[0-9]+)/', views.details, name='details'),
    path('add_event', views.add_Event, name='add_event'),
    path('(?P<event_id>[0-9]+)/comment/', views.comment, name='comment'),
    path('(?P<event_id>[0-9]+)/login/', views.login_input, name='login'),
    path('(?P<event_id>[0-9]+)/delete/', views.delete, name='delete'),



    ]