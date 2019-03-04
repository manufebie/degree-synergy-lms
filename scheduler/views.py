from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.utils.safestring import mark_safe
from .models import *
from .utils import Calendar

class CalendarView(ListView):
    model = Event
    template_name = 'scheduler/events.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use todays date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        html_cal = cal.format_month(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
