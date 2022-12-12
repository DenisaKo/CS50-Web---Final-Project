import datetime
from hour.models import Day
from django.contrib.auth.models import User


def create_day():
    today = datetime.date.today()
    users = User.objects.all()
    for user in users:
        if Day.objects.filter(user=user, date=today).first() == None:
            Day.objects.create(user=user, date=today, completed=True)
 