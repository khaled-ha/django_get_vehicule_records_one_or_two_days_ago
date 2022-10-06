from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import utc
import datetime
import calendar
from datetime import date
from .models import NavigationRecord , Vehicule
# Create your views here.
def get_date_range():
    pass

def get_records(request):
    today = date.today()
    year = today.year
    month = today.month
    day = today.day
    month_range = calendar.monthrange(year,month)
    target_day = 0
    if calendar.January == month:
        if day == 1:
            year_target = year - 1
            month_target = 12
            day_target = int(calendar.calendar(year_target).split(' ')[-1].split('/')[0])-2
            target_date = datetime.date(year_target, month_target, day_target)
        if day == 2:
            year_target = year - 1
            month_target = 12
            day_target = int(calendar.calendar(year_target).split(' ')[-1].split('/')[0])-1
            target_date = datetime.date(year_target, month_target, day_target)
        if day > 2 :
            target_day = day - 2
            target_date = datetime.date(year, month, target_day)
    else:
        if day > 2 :
            target_day = day - 2
        if day == 2 :
            target_day = month_range[1]
        if day == 1 :
            target_day = month_range[1] - 1
    
    target_date = datetime.date(year, month, target_day)
    vehicules = Vehicule.objects.filter(related_nav_rec__datetime__gte=target_date).all().distinct()
    data = [x.get_related_navigation_records for x in vehicules]
    return render(request, 'template/list_vec_rec.html',{'vehicules':vehicules,'data':data})