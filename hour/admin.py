from django.contrib import admin
from .models import Day, SickHour, Month

# Register your models here.
admin.site.register(Day)
admin.site.register(SickHour)
admin.site.register(Month)