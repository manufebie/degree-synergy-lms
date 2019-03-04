from django.urls import path

from . import views

app_name = 'scheduler'

urlpatterns = [
    path('', views.CalendarView.as_view(), name='events'),
]