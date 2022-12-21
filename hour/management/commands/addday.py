from django.core.management.base import BaseCommand, CommandError
from hour.models import Day, Month
from django.contrib.auth.models import User
import datetime

class Command(BaseCommand):

    def handle(self, *args, **options):
        today = datetime.date.today()
        month = today.month
        year = today.year
        users = User.objects.all()
        for user in users:
            month_db, created = Month.objects.get_or_create(user=user, month=month, year=year)
            day_db, created = Day.objects.get_or_create(user=user, date=today, month=month_db, completed=True)

# for pythonanywhere tasks:
# https://www.pythonanywhere.com/forums/topic/20964/
# cd ~ && source /home/Denisa/.virtualenvs/django4/bin/activate && cd /home/Denisa/CS50_Web_Final/CS50-Web---Final-Project && python manage.py addday



