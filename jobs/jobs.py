import datetime
from hour.models import Day
from django.contrib.auth.models import User


def create_day():
    today = datetime.date.today()
    users = User.objects.all()
    for user in users:
        if Day.objects.filter(user=user, date=today).first() == None:
            Day.objects.create(user=user, date=today, completed=True)
        # today_bd, created = Day.objects.get_or_create(user=user, date=today)
    # counter = 0
    # counter += 1
    # print(f"hello, it is working, {counter}")