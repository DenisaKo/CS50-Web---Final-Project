from .models import Day, Month

def counter(user, month, year):
    month_db, created = Month.objects.get_or_create(user=user, month=month, year=year)
    days = Day.objects.filter(user=user, month=month_db)

    sum_required = 0
    sum_extra = 0

    for day in days:
        sum_required += day.required
        sum_extra += day.extra

    month_db.required = sum_required
    month_db.extra = sum_extra
    month_db.save()