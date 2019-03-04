from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

class Calendar(HTMLCalendar):

    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    def format_day(self, day, events):
        '''
        Formats a day as a td and filters events by day
        '''
        d = ''
        for event in events.filter(start_time__day=day):
            d += f'<li>(event.title)</li>'
        
        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul><td>"
        return '<td></td>'

    def format_week(self, theweek, events):
        '''
        Formats a week as a tr
        '''
        week = ''
        for d, weekday in theweek:
            week += self.format_day(d, events)
        return f'<tr> {week} </tr>'

    def format_month(self, withyear=True):
        events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
		
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.format_week(week, events)}\n'
        return cal
