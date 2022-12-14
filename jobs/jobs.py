import datetime
from hour.models import Day, Month
from django.contrib.auth.models import User


def create_day():
    today = datetime.date.today()
    month = today.month
    year = today.year
    users = User.objects.all()
    for user in users:
        if Day.objects.filter(user=user, date=today).first() == None:
            Day.objects.create(user=user, date=today, completed=True)
            if Month.objects.filter(user=user, month=month, year=year).first() == None:
                Month.objects.create(user=user, month=month, year=year)
 