import datetime
from hour.models import Day, Month
from django.contrib.auth.models import User


def create_day():
    today = datetime.date.today()
    month = today.month
    year = today.year
    users = User.objects.all()
    for user in users:
            month_db, created = Month.objects.get_or_create(user=user, month=month, year=year)
            day_db, created = Day.objects.get_or_create(user=user, date=today, month=month_db, completed=True)
 